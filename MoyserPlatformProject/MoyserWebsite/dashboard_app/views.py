from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from account_app.models import Companion , DisabilityUser
from django.shortcuts import get_object_or_404
from .forms import CompanionForm
from django.contrib import messages

# from .models import Testimonial

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    companions = Companion.objects.all()
    return render(request, "dashboard_app/admin_dashboard.html", {'companions': companions})
    
# @login_required
# @user_passes_test(is_admin)
# def beneficiary_dashboard_view(request):
#     disability_users = DisabilityUser.objects.all() 
#     return render(request, "dashboard_app/beneficiary_dashboard.html", {'disability_users': disability_users})
    

# @login_required
# @user_passes_test(is_admin)
# def monitor_beneficiary_dashboard_view(request , beneficiary_id):
#     beneficiary = get_object_or_404(DisabilityUser, id=beneficiary_id)
#     return render(request, "dashboard_app/monitor_history_beneficiary.html", {"beneficiary": beneficiary})



@user_passes_test(is_admin)
def edit_companion_view(request, companion_id):
    companion = get_object_or_404(Companion, id=companion_id)
    
    if request.method == 'POST':
        form = CompanionForm(request.POST, request.FILES, instance=companion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Companion updated successfully!')
            return redirect('dashboard_app:admin_dashboard_view')  # Redirect to the admin dashboard
    else:
        form = CompanionForm(instance=companion)
    
    return render(request, "dashboard_app/edit_companion.html", {'form': form, 'companion': companion})

# View to delete a companion
@login_required
@user_passes_test(is_admin)
def delete_companion_view(request, companion_id):
    companion = get_object_or_404(Companion, id=companion_id)
    
    if request.method == 'POST':
        companion.delete()
        messages.success(request, 'Companion deleted successfully!')
        return redirect('dashboard_app:admin_dashboard_view')  # Redirect to the admin dashboard
    
    return render(request, "dashboard_app/confirm_delete_companion.html", {'companion': companion})