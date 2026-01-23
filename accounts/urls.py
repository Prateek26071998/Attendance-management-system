from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
    path("dashboard/hr/", views.hr_dashboard, name="hr_dashboard"),
    path("dashboard/employee/", views.employee_dashboard, name="employee_dashboard"),
]
