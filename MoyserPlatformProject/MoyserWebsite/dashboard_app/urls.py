from django.urls import path
from . import views

app_name = "dashboard_app"

urlpatterns = [
    path("admin/", views.admin_dashboard_view, name="admin_dashboard"),
    path("admin/beneficiary/", views.monitor_beneficiary_dashboard_view, name="beneficiary_dashboard"),
    path("admin/companion/", views.monitor_companion_dashboard_view, name="companion_dashboard"),
]
