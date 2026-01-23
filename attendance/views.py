from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import Attendance
from accounts.models import User


# ---------------- HR MARK ATTENDANCE ----------------
@login_required
def hr_attendance(request):
    if request.user.role != "HR":
        return redirect("/admin/")

    employees = User.objects.filter(role="EMPLOYEE")

    if request.method == "POST":
        emp_id = request.POST.get("employee")
        status = request.POST.get("status")

        Attendance.objects.create(
            user_id=emp_id,
            status=status
        )
        return redirect("/hr/attendance/")

    return render(
        request,
        "attendance/hr_attendance.html",
        {"employees": employees}
    )


# ---------------- HR ATTENDANCE REPORT ----------------
@login_required
def hr_attendance_report(request):
    if request.user.role != "HR":
        return redirect("/admin/")

    records = Attendance.objects.select_related("user").order_by("-date")

    return render(
        request,
        "attendance/hr_attendance_report.html",
        {"records": records}
    )


# ---------------- EMPLOYEE MARK TODAY ATTENDANCE ----------------
@login_required
def employee_attendance(request):
    if request.user.role != "EMPLOYEE":
        return redirect("/admin/")

    today = timezone.now().date()

    already_marked = Attendance.objects.filter(
        user=request.user,
        date=today
    ).exists()

    if request.method == "POST" and not already_marked:
        Attendance.objects.create(
            user=request.user,
            status="PRESENT"
        )
        return redirect("/hr/employee/attendance/")

    return render(
        request,
        "attendance/employee_attendance.html",
        {"already_marked": already_marked}
    )


# ---------------- EMPLOYEE VIEW MY ATTENDANCE ----------------
# ---------------- EMPLOYEE VIEW MY ATTENDANCE ----------------
@login_required
def employee_my_attendance(request):
    if request.user.role != "EMPLOYEE":
        return redirect("/login/")

    records = Attendance.objects.filter(
        user=request.user
    ).order_by("-date")

    return render(
        request,
        "attendance/employee_my_attendance.html",
        {"records": records}
    )
