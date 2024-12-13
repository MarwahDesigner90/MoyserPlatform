from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    return render(request, "dashboard_app/admin_dashboard.html")

@login_required
@user_passes_test(is_admin)
def monitor_beneficiary_dashboard_view(request):
    return render(request, "dashboard_app/beneficiary_dashboard.html")

@login_required
@user_passes_test(is_admin)
def monitor_companion_dashboard_view(request):
    return render(request, "dashboard_app/companion_dashboard.html")
