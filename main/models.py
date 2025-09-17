from django.db import models
from accounts.models import CustomUser
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

# Create your models here.
APPOINTMENT_STATUS = (
    ("Pending", "Pending"),
    ("Confirmed", "Confirmed"),
    ("Completed", "Completed"),
    ("Paid", "Paid"),
    ("Cancelled", "Cancelled"),
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        constraints = [
            UniqueConstraint(Lower("name"), name="unique_category_name_ci")
        ]

class Service(models.Model):
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={"user_role": 2}, related_name="services")
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "services"

    def __str__(self):
        return f"{self.title} - {self.provider.username}"


class Appointment(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={"user_role": 3}, related_name="appointments")
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={"user_role": 2}, related_name="service_provider")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default="Pending")
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'appointments'
        ordering = ["-appointment_date"]

    def __str__(self):
        return f"{self.service.title} - {self.customer.username} ({self.status})"