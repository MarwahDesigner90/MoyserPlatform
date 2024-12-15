from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from account_app.models import Companion
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.


@login_required
def book_companion_view(request, companion_id):
    companion = None
    while not companion:
        try:
            companion = User.objects.get(id=companion_id)
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
            companion=companion,
            booking_date_time=booking_date_time,

            address=address,
            status="pending"
        )


        return redirect("booking_app:companion_list")  # Redirect after successful booking

    context = {
        "companion": companion,
        "bookings_as_companion": companion.bookings_as_companion.all(),
    }
    return render(request, "booking_app/create_booking.html", context)


@login_required
def booking_history_user_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    context = {
        "user_bookings": user_bookings,
    }
    return render(request, "booking_app/user_booking_history.html", context)




def booking_history_companion_view(request):
    return render(request, 'booking_app/companion_booking_history.html')


# def companion_list_view(request):
#     """
#     View to list all available companions.
#     Users can select a companion to book from this list.
#     """
#     companions = Companion.objects.filter(availability=True)
#     return render(request, 'booking_app/companion_list.html', {'companions': companions})


