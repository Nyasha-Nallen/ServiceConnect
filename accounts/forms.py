from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profile


class ServiceProviderRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_role = CustomUser.UserRole.SERVICE_PROVIDER
        if commit:
            user.save()
            Profile.objects.filter(user=user).update(bio="New Service Provider")
        return user


class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_role = CustomUser.UserRole.CUSTOMER
        if commit:
            user.save()
            Profile.objects.filter(user=user).update(bio="New Customer")
        return user
