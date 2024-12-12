from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Companion, DisabilityUser, Skill

# Create your views here.

def profile_beneficiary_view(request: HttpRequest):
    if request.user.is_authenticated:
        disability_user = get_object_or_404(DisabilityUser, user=request.user)
        return render(request, "account_app/profile_beneficiary.html", {"disability_user": disability_user})
    return redirect("sign_in_user_view")

def sign_up_beneficiary_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        disability_type = request.POST.get("disability_type")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        address = request.POST.get("address")

        user = User.objects.create_user(username=username, password=password)
        DisabilityUser.objects.create(
            user=user,
            phone_number=phone_number,
            disability_type=disability_type,
            gender=gender,
            age=age,
            address=address
        )
        messages.success(request, "Account created successfully!")
        return redirect("sign_in_user_view")

    return render(request, "account_app/sign_up_beneficiary.html")

def profile_companion_view(request: HttpRequest):
    if request.user.is_authenticated:
        companion = get_object_or_404(Companion, user=request.user)
        return render(request, "account_app/profile_companion.html", {"companion": companion})
    return redirect("sign_in_user_view")

def sign_up_companion_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()  # Get and strip any extra spaces
        if not username:  # Check if username is empty
            messages.error(request, "Username is required.")
            return render(request, "account_app/sign_up_companion.html")

        password = request.POST.get("password")
        bank_account = request.POST.get("bank_account")
        availability = request.POST.get("availability") == "on"
        hour_rent = request.POST.get("hour_rent")
        skills = request.POST.getlist("skills")
        city = request.POST.get("city")
        certification = request.FILES.get("certification")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        age = request.POST.get("age")

        try:
            user = User.objects.create_user(username=username, password=password)
        except ValueError as e:
            messages.error(request, str(e))
            return render(request, "account_app/sign_up_companion.html")

        companion = Companion.objects.create(
            user=user,
            bank_account=bank_account,
            availability=availability,
            hour_rent=hour_rent,
            city=city,
            certification=certification,
            phone_number=phone_number,
            gender=gender,
            age=age
        )
        companion.skills.set(Skill.objects.filter(id__in=skills))
        messages.success(request, "Companion account created successfully!")
        return redirect("sign_in_user_view")

    skills = Skill.objects.all()
    return render(request, "account_app/sign_up_companion.html", {"skills": skills})

def sign_in_user_view(request: HttpRequest):
    return render(request, "account_app/sign_in_user.html")

@login_required
def edit_companion_profile_view(request: HttpRequest):
    companion = get_object_or_404(Companion, user=request.user)
    if request.method == "POST":
        companion.bank_account = request.POST.get("bank_account")
        companion.availability = request.POST.get("availability") == "on"
        companion.hour_rent = request.POST.get("hour_rent")
        companion.city = request.POST.get("city")
        companion.phone_number = request.POST.get("phone_number")
        companion.gender = request.POST.get("gender")
        companion.age = request.POST.get("age")
        companion.certification = request.FILES.get("certification") or companion.certification
        skills = request.POST.getlist("skills")
        companion.skills.set(Skill.objects.filter(id__in=skills))
        companion.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile_companion_view")

    skills = Skill.objects.all()
    return render(request, "account_app/edit_companion_profile.html", {"companion": companion, "skills": skills})

@login_required
def edit_beneficiary_profile_view(request: HttpRequest):
    disability_user = get_object_or_404(DisabilityUser, user=request.user)
    if request.method == "POST":
        disability_user.phone_number = request.POST.get("phone_number")
        disability_user.disability_type = request.POST.get("disability_type")
        disability_user.gender = request.POST.get("gender")
        disability_user.age = request.POST.get("age")
        disability_user.address = request.POST.get("address")
        disability_user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile_beneficiary_view")

    return render(request, "account_app/edit_beneficiary_profile.html", {"disability_user": disability_user})
