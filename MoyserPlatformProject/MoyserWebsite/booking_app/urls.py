from django.urls import path
from . import views

app_name = 'booking_app'

urlpatterns = [
    path('', views.companion_list_view, name='companion_list'),
    path('book/', views.book_companion_view, name='book_companion'),
    path('user/', views.booking_history_user_view, name='booking_history_user'),
    path('companion/', views.booking_history_companion_view, name='booking_history_companion'),
    path('book/<int:companion_id>/', views.book_companion_view, name='book_companion'),
    path("payment/<int:booking_id>/", views.payment_view, name="payment"),
    path('add-feedback/<int:companion_id>/', views.add_feedback_view, name='add_feedback'),
    path('view-feedback/<int:companion_id>/', views.view_feedback_view, name='view_feedback'),
    path('booking_history/', views.booking_history_view, name='booking_history'),
    

]