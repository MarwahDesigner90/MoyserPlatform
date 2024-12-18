from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from .models import User, Companion, DisabilityUser, Skill


#Profile for Beneficiary
@login_required
def profile_beneficiary_view(request: HttpRequest):
    if request.user.role == "beneficiary":
        try:
            disability_user = DisabilityUser.objects.get(user=request.user)
            return render(request, "account_app/profile_beneficiary.html", {"disability_user": disability_user})

        except DisabilityUser.DoesNotExist:
            messages.error(request, "No user profile found.")
    return redirect("account_app:sign_in_user_view")






# Sign Up for Beneficiary
def sign_up_beneficiary_view(request: HttpRequest):
    cities = [choice[0] for choice in DisabilityUser.CITY_CHOICES]  

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        disability_type = request.POST.get("disability_type")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        city = request.POST.get("city")
        address = request.POST.get("address")

        try:
            user = User.objects.create_user(username=username, password=password, role="beneficiary")
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            DisabilityUser.objects.create(
                user=user,
                email=user.email,
                phone_number=phone_number,
                disability_type=disability_type,
                gender=gender,
                age=age,
                city=city,
                address=address,
            )
            messages.success(request, "Beneficiary account created successfully!")
            return redirect("account_app:sign_in_user_view")
        except Exception as e:
            messages.error(request, f"Error creating account: {e}")
            return render(request, "account_app/sign_up_beneficiary.html", {"cities": cities})

    return render(request, "account_app/sign_up_beneficiary.html", {"cities": cities})



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
    cities = [choice[0] for choice in DisabilityUser.CITY_CHOICES]  # Fetch city list
    skills = Skill.objects.all()

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        bank_account = request.POST.get("bank_account")
        hour_rent = request.POST.get("hour_rent")
        skills = request.POST.getlist("skills")  # Multi-select skills
        city = request.POST.get("city")
        certification = request.FILES.get("certification")
        phone_number = request.POST.get("phone_number")
        gender = request.POST.get("gender")
        age = request.POST.get("age")

        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            companion = Companion.objects.create(
                companion=user,
                bank_account=bank_account,
                hour_rent=hour_rent,
                city=city,
                certification=certification,
                phone_number=phone_number,
                gender=gender,
                age=age
            )

            # Assign selected skills
            companion.skills.set(Skill.objects.filter(id__in=skills))
            messages.success(request, "Companion account created successfully!")
            return redirect("account_app:sign_in_user_view")
        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, f"Error: {e}")

    return render(request, "account_app/sign_up_companion.html", {"cities": cities, "skills": skills})
# Sign In for all
def sign_in_user_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect("dashboard_app:admin_dashboard_view")  # Redirect admins to their dashboard
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
        availability = request.POST.get("availability") 
        companion.availability = True if availability == 'online' else False 
        companion.hour_rent = request.POST.get("hour_rent")
        companion.city = request.POST.get("city")
        skills = request.POST.getlist("skills")  # Get selected skills
        
        companion.skills.set(Skill.objects.filter(id__in=skills))  # Update skills

        companion.save()  # Save the updated data
        messages.success(request, "Profile updated successfully!")
        return redirect("account_app:profile_companion_view")  # Redirect to the profile page

    # Get all skills to populate in the edit form
    skills = Skill.objects.all()
    print(skills)
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
        disability_user.city = request.POST.get("city")         
        disability_user.save()
        messages.success(request, "Beneficiary profile updated successfully!")
        return redirect("account_app:profile_beneficiary_view")

    return render(request, "account_app/edit_beneficiary_profile.html", {"disability_user": disability_user})

def logout_view(request):
    logout(request)
    return redirect('main_app:home_view')