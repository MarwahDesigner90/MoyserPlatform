from . import views 
from django.urls import path

app_name = 'dashboard_app'

urlpatterns = [ 
    path("monitor/beneficiary/",views.monitor_history_beneficiary_view , name="monitor_history_beneficiary_view"),
    path("admin/dashboard/",views.admin_dashboard_view,name="admin_dashboard_view"),
    path("feedback/",views.feedback_view, name="feedback_view"),
]