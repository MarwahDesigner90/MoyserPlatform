from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from account_app.models import Companion
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages

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

        # Save booking to the database
        Booking.objects.create(
            user=request.user,
            companion=companion.companion,
            booking_date_time=booking_date_time,
            address=address,
            status="pending"
        )


        return redirect("booking_app:companion_list")  # Redirect after successful booking


    context = {
        "companion": companion,
        "bookings_as_companion": Booking.objects.filter(companion=companion.id),
    }
    return render(request, "booking_app/create_booking.html", context)


@login_required
def booking_history_user_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
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




def companion_list_view(request):
    """
    View to list all available companions.
    Users can select a companion to book from this list.
    """
    companions = Companion.objects.filter(availability=True)
    return render(request, 'booking_app/companion_list.html', {'companions': companions})


