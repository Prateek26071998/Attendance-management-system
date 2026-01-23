from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            if user.role == "ADMIN":
                return redirect("/dashboard/admin/")
            elif user.role == "HR":
                return redirect("/dashboard/hr/")
            else:
                return redirect("/dashboard/employee/")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password"}
        )

    return render(request, "accounts/login.html")


# ---------------- LOGOUT ----------------
@login_required
def logout_view(request):
    logout(request)
    return redirect("/login/")


# ---------------- ADMIN DASHBOARD ----------------
@login_required
def admin_dashboard(request):
    if request.user.role != "ADMIN":
        return redirect("/login/")
    return render(request, "accounts/admin_dashboard.html")


# ---------------- HR DASHBOARD ----------------
@login_required
def hr_dashboard(request):
    if request.user.role != "HR":
        return redirect("/login/")
    return render(request, "accounts/hr_dashboard.html")


# ---------------- EMPLOYEE DASHBOARD ----------------
@login_required
def employee_dashboard(request):
    if request.user.role != "EMPLOYEE":
        return redirect("/login/")
    return render(request, "accounts/employee_dashboard.html")
