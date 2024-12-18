from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from account_app.models import Companion, Skill ,  DisabilityUser
# from .models import Testimonial
# Create your views here.

def home_view(request:HttpRequest):
    cities=Companion.CITY_CHOICES
    genders=Companion.GENDER_CHOICES

    return render(request,"main_app/home.html",{'cities': cities , 'genders': genders})

def companions_list_view (request:HttpRequest):

    companions = Companion.objects.all()  
  

    search_city = request.GET.get('city', '')
    search_gender = request.GET.get('gender', '')
    search_disability_type = request.GET.get('disability_type', '')

    # Apply filters based on the search query
    companions = Companion.objects.filter(availability=True)

    if search_city:
        companions = companions.filter(city__icontains=search_city)

    if search_gender:
        companions = companions.filter(gender__icontains=search_gender)
    
    if search_disability_type:
        companions = companions.filter(disability_type=search_disability_type)

    # Get all unique cities for the filter dropdown
    cities = Companion.CITY_CHOICES
    print(Companion.CITY_CHOICES)
    return render(request, 'main_app/companions_list.html', {
        'companions': companions,
        'cities': cities,
        'search_city': search_city,
        'search_gender': search_gender,
        'search_disability_type': search_disability_type,
    })




