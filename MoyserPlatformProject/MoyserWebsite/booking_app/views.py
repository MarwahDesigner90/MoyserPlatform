from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Payment
from account_app.models import Companion, DisabilityUser
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404
import stripe
from django.conf import settings
from django.db.models import Q
from .forms import FeedbackForm
from main_app.models import Feedback



# Create your views here.
@login_required
def book_companion_view(request, companion_id):
    companion = None
    while not companion:
        try:
            companion = Companion.objects.get(id=companion_id)
        except User.DoesNotExist:
            return redirect("booking_app:companion_list")  # Redirect if companion is not found

    if request.method == "POST":
        booking_date = request.POST.get("booking_date")
        booking_time = request.POST.get("booking_time")
        address = request.POST.get("address")

        # Combine booking date and time
        booking_date_time = timezone.datetime.strptime(
            f"{booking_date} {booking_time}", "%Y-%m-%d %H:%M"
        )

        # Set the end time to be one hour after the booking date and time
        end_booking_date_time = booking_date_time + timezone.timedelta(hours=1)

        # Check if there's already a booking for the same companion at the selected time
        if Booking.objects.filter(
            companion=companion.companion, 
            booking_date_time__lt=end_booking_date_time,  # Ensure the new booking's end time doesn't overlap with existing bookings
            end_booking_date_time__gt=booking_date_time,  # Ensure the new booking's start time doesn't overlap with existing bookings
        ).exists():
            messages.error(request, "This time slot is already booked. Please choose a different time.")
            return redirect('booking_app:book_companion', companion_id=companion.id)  # Stay on the booking page

        # Save booking to the database with the start and end times
        booking = Booking.objects.create(
            user=request.user,
            companion=companion.companion,
            booking_date_time=booking_date_time,
            end_booking_date_time=end_booking_date_time,  # Store the end time
            address=address,
            status="pending"
        )

        return redirect(reverse('booking_app:payment', args=[booking.id]))  # Redirect after successful booking

    context = {
        "companion": companion,
        "bookings_as_companion": Booking.objects.filter(companion=companion.id),
    }
    return render(request, "booking_app/create_booking.html", context)


@login_required
def booking_history_user_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    
    # Ensure only confirmed bookings are visible for feedback
    user_bookings = user_bookings.filter(status="CONFIRMED")
    
    context = {
        "user_bookings": user_bookings,
    }
    return render(request, "booking_app/user_booking_history.html", context)

@login_required
def booking_history_companion_view(request):
    try:
        companion = Companion.objects.get(companion=request.user)
    except Companion.DoesNotExist:
        
        messages.error(request, "You can't access this page.")
        return redirect('booking_app:companion_list')

    companion_bookings = Booking.objects.filter(companion=companion.companion)

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        action = request.POST.get('action')
        try:
            booking = Booking.objects.get(id=booking_id)

            if action == 'accept':
                booking.status = 'CONFIRMED'
                
            elif action == 'reject':
                booking.status = 'CANCELLED'
                
            booking.save()
            
            return redirect('booking_app:booking_history_companion')

        except Booking.DoesNotExist:
            messages.error(request, "The booking you're trying to modify does not exist.")
            return redirect('booking_app:booking_history_companion')

    context = {
        "companion_bookings": companion_bookings,
    }
    return render(request, 'booking_app/companion_booking_history.html', context)




@login_required
def companion_list_view(request):
    """
    View to list all available companions with search functionality.
    Users can filter companions by city and gender.
    """
    search_city = request.GET.get('city', '')
    search_gender = request.GET.get('gender', '')

    companions = Companion.objects.filter(availability=True)

    # Apply filters based on the search query
    if search_city:
        companions = companions.filter(city__icontains=search_city)

    if search_gender:
        companions = companions.filter(gender__icontains=search_gender)

    # Get all unique cities for the filter dropdown
    cities = [choice[0] for choice in Companion.CITY_CHOICES]

    return render(request, 'booking_app/companion_list.html', {
        'companions': companions,
        'cities': cities,
        'search_city': search_city,
        'search_gender': search_gender
    })

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def payment_view(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    companion = booking.companion.compinon_user
    amount = int(companion.hour_rent * 100)  # Convert to halalas (Stripe requires this)

    if request.method == "POST":
        token = request.POST.get("stripeToken")  # Stripe's generated token for the card
        card_name = request.POST.get("card_name")

        try:
            # Create a charge with Stripe
            charge = stripe.Charge.create(
                amount=amount,
                currency="SAR",
                description=f"Payment for booking {booking.id}",
                source=token,  # Token generated by Stripe.js
            )

            # Save the payment in your database
            Payment.objects.create(
                booking=booking,
                status="completed",
                
            )

            # Update booking status
            booking.status = "CONFIRMED"
            booking.save()

            messages.success(request, "Payment successful!")
            return redirect("booking_app:booking_history_user")

        except stripe.error.StripeError as e:
            messages.error(request, f"Payment failed: {e}")
            return redirect("booking_app:payment", booking_id=booking.id)

    context = {
        "booking": booking,
        "amount": amount / 100,  # Convert back to dollars for display
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, "booking_app/payment.html", context)


@login_required
def add_feedback_view(request, companion_id):
    companion = get_object_or_404(Companion, id=companion_id)

    # Get the user's latest booking for this companion
    user_booking = Booking.objects.filter(user=request.user, companion=companion.companion).last()

    # Check if the booking status is CONFIRMED
    if not user_booking or user_booking.status != 'CONFIRMED':
        messages.error(request, "You can only leave a review after the booking has been confirmed.")
        return redirect('booking_app:booking_history_user')  # Redirect to booking history

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.disability_user = DisabilityUser.objects.get(user=request.user)  # Assuming the user is a disability user
            feedback.companion = companion
            feedback.save()
            messages.success(request, "Feedback added successfully!")
            return redirect('booking_app:companion_list')  # Redirect to the list of companions
    else:
        form = FeedbackForm()

    return render(request, "booking_app/add_feedback.html", {"form": form, "companion": companion})


# View to list feedback for a specific companion
def view_feedback_view(request, companion_id):
    companion = get_object_or_404(Companion, id=companion_id)
    feedbacks = Feedback.objects.filter(companion=companion).all()
    return render(request, "booking_app/view_feedback.html", {"companion": companion, "feedbacks": feedbacks})