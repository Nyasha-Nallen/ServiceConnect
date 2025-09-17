from django.shortcuts import redirect
from functools import wraps
from django.contrib import messages

def role_required(allowed_roles=None):
    """
    Restrict access to views based on user_role.
    """
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
                # 🚨 Redirect to correct dashboard if wrong role
                messages.warning(request, "You are not allowed to access that page. Redirected to your dashboard.")
                return redirect(get_dashboard_url(request.user.user_role))
            return redirect("index")
        return wrapper
    return decorator


def get_dashboard_url(user_role):
    """
    Return the correct dashboard URL based on user role.
    """
    if user_role == 1:
        return "admin_dashboard"
    elif user_role == 2:
        return "provider_dashboard"
    elif user_role == 3:
        return "customer_dashboard"
    return "index"
