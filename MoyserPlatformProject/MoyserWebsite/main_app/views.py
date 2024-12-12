from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def home_view(request:HttpRequest):

    return render(request,"main_app/home.html")

def companions_list_view (request:HttpRequest):

    return render(request,"main_app/companions_list.html")

def reviews_companion_view (request:HttpRequest):

    return render(request,"main_app/reviews_companion.html")

