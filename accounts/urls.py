from django.urls import path
from . import views

urlpatterns = [
    path("register/service-provider/", views.register_service_provider, name="register_service_provider"),
    path("register/customer/", views.register_customer, name="register_customer"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

]
