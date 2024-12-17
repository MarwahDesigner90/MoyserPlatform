from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from account_app.models import Companion, Skill ,  DisabilityUser
# from .models import Testimonial
# Create your views here.

def home_view(request:HttpRequest):
# adding filter code here  
    # testimonials = Testimonial.objects.all().order_by('-created_at')[:10]  # Limit to 10 recent testimonials
    return render(request,"main_app/home.html")

def companions_list_view (request:HttpRequest):
# adding filter code here 
    companions = Companion.objects.all()  # Start with all companions
    # skills = Skill.objects.all()  # Get all skills for the dropdown

    # # Get filter criteria from query parameters
    # city = request.GET.get('city')
    # skill_name = request.GET.get('skills')
    # disability_type = request.GET.get('disability_type')

    # # Apply filters based on user selection
    # if city:
    #     companions = companions.filter(city=city)
    # if skill_name:
    #     companions = companions.filter(skills__name=skill_name)
    # if disability_type:
    #     companions = companions.filter(companion__disabilityuser__disability_type=disability_type)

    # return render(request, "main_app/companions_list.html", {
    #     'companions': companions,
    #     'skills': skills,
    #     'selected_city': city,
    #     'selected_skill': skill_name,
    #     'selected_disability': disability_type,
    #     'CITY_CHOICES': Companion.CITY_CHOICES,  # Pass CITY_CHOICES to the template
    # })

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
    cities = Companion.objects.values_list('city', flat=True).distinct()

    return render(request, 'main_app/companions_list.html', {
        'companions': companions,
        'cities': cities,
        'search_city': search_city,
        'search_gender': search_gender,
        'search_disability_type': search_disability_type,
    })


def reviews_companion_view (request:HttpRequest):

    return render(request,"main_app/reviews_companion.html")


