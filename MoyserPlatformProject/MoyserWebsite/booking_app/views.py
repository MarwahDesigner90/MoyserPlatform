from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking
# Create your views here.

@login_required
def book_companion_view(request):
    return render(request, 'booking_app/create_booking.html')


def booking_history_user_view(request):
    return render(request, 'booking_app/user_booking_history.html')

@login_required
def booking_history_companion_view(request):
    return render(request, 'booking_app/companion_booking_history.html')

@login_required
def companion_list_view(request):
    return render(request, 'booking_app/companion_list.html')