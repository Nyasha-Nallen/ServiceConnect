from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import ServiceProviderRegistrationForm, CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register_service_provider(request):
    if request.method == "POST":
        form = ServiceProviderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your Account has been created successfully!. Login here')
            return redirect("login")  
    else:
        form = ServiceProviderRegistrationForm()
    return render(request, "accounts/register_service_provider.html", {"form": form})


def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your Account has been created successfully!. Login here')
            return redirect("login") 
    else:
        form = CustomerRegistrationForm()
    return render(request, "accounts/register_customer.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")

            # Redirect based on role
            if user.user_role == 1:
                return redirect("admin_dashboard")
            elif user.user_role == 2:
                return redirect("provider_dashboard")
            elif user.user_role == 3:
                return redirect("customer_dashboard")
            else:
                messages.warning(request, "Unknown role. Redirecting to home.")
                return redirect("index")  # fallback
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

@login_required
def user_logout(request):
    """
    Logs out the currently logged-in user and redirects to login page
    """
    logout(request)
    return redirect("index")
