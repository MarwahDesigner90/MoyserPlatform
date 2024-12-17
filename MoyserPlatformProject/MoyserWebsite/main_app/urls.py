from . import views 
from django.urls import path

app_name = 'main_app'

urlpatterns = [ 
    path("",views.home_view,name="home_view"),
    # path("companions/list/",views.companions_list_view , name="companions_list_view"),
    # path("companion/reviews/",views.reviews_companion_view ,name="reviews_companion_view"),
    
]