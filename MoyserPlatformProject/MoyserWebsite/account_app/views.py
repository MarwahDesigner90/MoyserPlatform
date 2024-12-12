from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def profile_beneficiary_view(request:HttpRequest):

    return render(request,"account_app/profile_beneficiary.html")

def sign_up_beneficiary_view(request:HttpRequest):

    return render(request,"account_app/sign_up_beneficiary.html")

def profile_companion_view(request:HttpRequest):

    return render(request,"account_app/profile_companion.html")

def sign_up_companion_view(request:HttpRequest):

    return render(request,"account_app/sign_up_companion.html")

def sign_in_user_view (request:HttpRequest):

    return render(request,"account_app/sign_in_user.html")



