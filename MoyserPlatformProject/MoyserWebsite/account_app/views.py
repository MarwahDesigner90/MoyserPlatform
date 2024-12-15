from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Companion, DisabilityUser, Skill


# Profile for Beneficiary
@login_required
def profile_beneficiary_view(request: HttpRequest):
    if request.user.role == "beneficiary":
        disability_user = get_object_or_404(DisabilityUser, user=request.user)
        return render(request, "account_app/profile_beneficiary.html", {"disability_user": disability_user})
    return redirect("account_app:sign_in_user_view")


# Sign Up for Beneficiary
def sign_up_beneficiary_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        disability_type = request.POST.get("disability_type")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        address = request.POST.get("address")

        try:
            user = User.objects.create_user(username=username, password=password, role="beneficiary")
            DisabilityUser.objects.create(
                user=user,
                phone_number=phone_number,
                disability_type=disability_type,
                gender=gender,
                age=age,
                address=address
            )
            messages.success(request, "Beneficiary account created successfully!")
            return redirect("account_app:sign_in_user_view")
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return render(request, "account_app/sign_up_beneficiary.html")

    return render(request, "account_app/sign_up_beneficiary.html")


@login_required
def profile_companion_view(request: HttpRequest):
    if request.user.role == "companion":
        try:
            companion = Companion.objects.get(companion=request.user)
            return render(request, "account_app/profile_companion.html", {"companion": companion})
        except Companion.DoesNotExist:
            messages.error(request, "No Companion profile found. Please contact support or create a profile.")
            return redirect("account_app:sign_up_companion_view")
    return redirect("account_app:sign_in_user_view")


# Sign Up for Companion
def sign_up_companion_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        if not username:
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
            user = User.objects.create_user(username=username, password=password, role="companion")
            companion = Companion.objects.create(
                companion=user,
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
            return redirect("account_app:sign_in_user_view")
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return render(request, "account_app/sign_up_companion.html")

    skills = Skill.objects.all()
    return render(request, "account_app/sign_up_companion.html", {"skills": skills})


# Sign In for all
def sign_in_user_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("dashboard_app:admin_dashboard")  # Redirect admins to their dashboard
            elif user.role == "companion":
                return redirect("account_app:profile_companion_view")
            elif user.role == "beneficiary":
                return redirect("account_app:profile_beneficiary_view")
            else:
                return redirect("home")  # Default redirect for other roles
        else:
            messages.error(request, "Invalid username or password")
            return render(request, "account_app/sign_in_user.html")
    return render(request, "account_app/sign_in_user.html")


@login_required
def edit_companion_profile_view(request):
    # Get the logged-in user's companion object
    companion = get_object_or_404(Companion, companion=request.user)

    if request.method == "POST":
        # Update the companion's profile fields from the POST request
        companion.phone_number = request.POST.get("phone_number")
        companion.gender = request.POST.get("gender")
        companion.age = request.POST.get("age")
        companion.hour_rent = request.POST.get("hour_rent")
        companion.city = request.POST.get("city")
        skills = request.POST.getlist("skills")  # Get selected skills
        companion.skills.set(Skill.objects.filter(id__in=skills))  # Update skills

        companion.save()  # Save the updated data
        messages.success(request, "Profile updated successfully!")
        return redirect("account_app:profile_companion_view")  # Redirect to the profile page

    # Get all skills to populate in the edit form
    skills = Skill.objects.all()
    return render(request, "account_app/edit_companion_profile.html", {"companion": companion, "skills": skills})


# Edit Profile for Beneficiary
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
        messages.success(request, "Beneficiary profile updated successfully!")
        return redirect("account_app:profile_beneficiary_view")

    return render(request, "account_app/edit_beneficiary_profile.html", {"disability_user": disability_user})
