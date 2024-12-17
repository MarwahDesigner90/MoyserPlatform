from django.urls import path
from . import views

app_name = "dashboard_app"

urlpatterns = [
    path("admin/", views.admin_dashboard_view, name="admin_dashboard_view"),
    path("admin/beneficiary/", views.beneficiary_dashboard_view, name="beneficiary_dashboard_view"),
    path("admin/monitor/<beneficiary_id>/", views.monitor_beneficiary_dashboard_view, name="monitor_beneficiary_dashboard_view"),
]
