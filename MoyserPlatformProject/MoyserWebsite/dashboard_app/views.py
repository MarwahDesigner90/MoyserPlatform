from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.
def admin_dashboard_view(request:HttpRequest):

    return render(request,"dashboard_app/admin_dashboard.html")

def monitor_history_beneficiary_view(request:HttpRequest):

    return render(request,"dashboard_app/monitor_history_beneficiary.html")

def feedback_view(request:HttpRequest):

    return render(request,"dashboard_app/feedback.html")

