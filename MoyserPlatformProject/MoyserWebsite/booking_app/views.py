from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking
from account_app.models import CompanionUser

# Create your views here.


def book_companion_view(request):
    return render(request, "booking_app/create_booking.html")

def booking_history_user_view(request):
    return render(request, 'booking_app/user_booking_history.html')

def booking_history_companion_view(request):
    return render(request, 'booking_app/companion_booking_history.html')


def companion_list_view(request):
    """
    View to list all available companions.
    Users can select a companion to book from this list.
    """
    companions = CompanionUser.objects.all()
    return render(request, 'booking_app/companion_list.html', {'companions': companions})