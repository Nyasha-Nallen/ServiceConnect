from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class UserRole(models.IntegerChoices):
        SYST_ADMIN = 1, "SystAdmin"
        SERVICE_PROVIDER = 2, "ServiceProvider"
        CUSTOMER = 3, "Customer"

    email = models.EmailField(unique=True)
    user_role = models.PositiveSmallIntegerField(choices=UserRole.choices, default=UserRole.SYST_ADMIN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Use email as login field
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # still need username since we extend AbstractUser

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.email} ({self.get_user_role_display()})"


class Profile(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    #avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "profiles"

    def __str__(self):
        return f"Profile of {self.user.email}"
