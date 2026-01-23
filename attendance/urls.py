from django.urls import path
from . import views

urlpatterns = [
    path("attendance/", views.hr_attendance, name="hr_attendance"),
    path("attendance/report/", views.hr_attendance_report, name="hr_attendance_report"),
    path("employee/attendance/", views.employee_attendance, name="employee_attendance"),
    path("employee/my-attendance/", views.employee_my_attendance, name="employee_my_attendance"),
]
