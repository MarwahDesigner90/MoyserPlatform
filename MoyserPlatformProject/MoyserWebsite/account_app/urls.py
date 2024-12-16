from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'account_app'  # Namespace for the app

urlpatterns = [
    path("profile/beneficiary/", views.profile_beneficiary_view, name="profile_beneficiary_view"),
    path("signup/beneficiary/", views.sign_up_beneficiary_view, name="sign_up_beneficiary_view"),
    path("profile/companion/edit/", views.edit_companion_profile_view, name="edit_companion_profile_view"),
    path("profile/companion/", views.profile_companion_view, name="profile_companion_view"),
    path("signup/companion/", views.sign_up_companion_view, name="sign_up_companion_view"),
    path("profile/beneficiary/edit/", views.edit_beneficiary_profile_view, name="edit_beneficiary_profile_view"), 
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path("sign-in/", views.sign_in_user_view, name="sign_in_user_view"), 
]
