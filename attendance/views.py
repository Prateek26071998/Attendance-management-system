from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from collections import defaultdict

from .models import Attendance
from accounts.models import User


# ---------------- HR MARK ATTENDANCE ----------------

from datetime import time

@login_required
def hr_attendance(request):

    if request.user.role != "HR":
        return redirect("/admin/")

    employees = User.objects.filter(role="EMPLOYEE")
    today = timezone.now().date()
    current_time = timezone.localtime().time()

    if request.method == "POST":

        emp_id = request.POST.get("employee")
        status = request.POST.get("status")

        already_marked = Attendance.objects.filter(
            employee_id=emp_id,
            date=today
        ).exists()

        if already_marked:
            messages.error(request, "Attendance already marked for today!")

        else:
            # 🔥 Late attendance logic
            if status == "PRESENT" and current_time > time(10, 0):
                status = "LATE"

            Attendance.objects.create(
                employee_id=emp_id,
                date=today,
                status=status
            )

            if status == "LATE":
                messages.warning(request, "Marked as LATE (after 10 AM)")
            else:
                messages.success(request, "Attendance marked successfully!")

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
        return redirect("/login/")

    month = request.GET.get("month")
    year = request.GET.get("year")

    records = Attendance.objects.select_related("employee")

    if month and month.isdigit():
        records = records.filter(date__month=int(month))

    if year and year.isdigit():
        records = records.filter(date__year=int(year))

    records = records.order_by("employee__email", "-date")

    employee_records = {}

    for record in records:

        emp = record.employee

        if emp not in employee_records:
            employee_records[emp] = {
                "records": [],
                "present_count": 0,
                "absent_count": 0,
                "percentage": 0
            }

        employee_records[emp]["records"].append(record)

        if record.status == "PRESENT":
            employee_records[emp]["present_count"] += 1
        else:
            employee_records[emp]["absent_count"] += 1

    # calculate percentage
    for emp in employee_records:

        present = employee_records[emp]["present_count"]
        absent = employee_records[emp]["absent_count"]

        total = present + absent

        if total > 0:
            employee_records[emp]["percentage"] = round((present / total) * 100, 2)

    context = {
        "employee_records": employee_records,
        "selected_month": month,
        "selected_year": year,
    }

    return render(
        request,
        "attendance/hr_attendance_report.html",
        context
    )


# ---------------- EMPLOYEE VIEW MY ATTENDANCE DASHBOARD ----------------

@login_required
def employee_my_attendance(request):

    if request.user.role != "EMPLOYEE":
        return redirect("/login/")

    month = request.GET.get("month")
    year = request.GET.get("year")

    records = Attendance.objects.filter(
        employee=request.user
    )

    if month:
        records = records.filter(date__month=month)

    if year:
        records = records.filter(date__year=year)

    records = records.order_by("-date")

    present_count = records.filter(status__in=["PRESENT", "LATE"]).count()
    late_count = records.filter(status="LATE").count()
    absent_count = records.filter(status="ABSENT").count()

    total = present_count + absent_count

    if total > 0:
        attendance_percentage = round((present_count / total) * 100, 2)
    else:
        attendance_percentage = 0

    context = {
        "records": records,
        "present_count": present_count,
        "absent_count": absent_count,
        "attendance_percentage": attendance_percentage,
        "selected_month": month,
        "selected_year": year,
    }

    return render(
        request,
        "attendance/employee_my_attendance.html",
        context
    )