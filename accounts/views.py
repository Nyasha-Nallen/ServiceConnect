from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import ServiceProviderRegistrationForm, CustomerRegistrationForm


def register_service_provider(request):
    if request.method == "POST":
        form = ServiceProviderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("dashboard")  # redirect to dashboard
    else:
        form = ServiceProviderRegistrationForm()
    return render(request, "accounts/register_service_provider.html", {"form": form})


def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomerRegistrationForm()
    return render(request, "accounts/register_customer.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def user_logout(request):
    """
    Logs out the currently logged-in user and redirects to login page
    """
    logout(request)
    return redirect("login")
