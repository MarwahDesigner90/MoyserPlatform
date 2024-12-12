from . import views 
from django.urls import path

app_name = 'account_app'

urlpatterns = [ 
    path("profile/beneficiary/",views.profile_beneficiary_view,name="profile_beneficiary_view"),
    path("signup/beneficiary/",views.sign_up_beneficiary_view ,name="sign_up_beneficiary_view"),
    path("profile/companion/",views.profile_companion_view,name="profile_companion_view"),
    path("signup/companion/",views.sign_up_companion_view,name="sign_up_companion_view"),
    path("signin/user/",views.sign_in_user_view , name="sign_in_user_view"),

]