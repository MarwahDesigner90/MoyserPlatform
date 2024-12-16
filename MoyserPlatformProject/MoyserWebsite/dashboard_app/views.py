from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from account_app.models import Companion , DisabilityUser

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard_view(request):

    companions = Companion.objects.all()  # Get all companions
    return render(request, "dashboard_app/admin_dashboard.html", {'companions': companions})
    
@login_required
@user_passes_test(is_admin)
def monitor_beneficiary_dashboard_view(request):

    disability_users = DisabilityUser.objects.all()  # Get all disability users
    return render(request, "dashboard_app/beneficiary_dashboard.html", {'disability_users': disability_users})
    

@login_required
@user_passes_test(is_admin)
def monitor_companion_dashboard_view(request):
    return render(request, "dashboard_app/companion_dashboard.html")

