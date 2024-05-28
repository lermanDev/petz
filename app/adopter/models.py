from django.db import models
from django.contrib.auth.models import AbstractUser


# class Adopter(AbstractUser):
#     email = models.EmailField(unique=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


class Adopter(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email Address")


class AdopterProfile(BaseModel):
    adopter = models.OneToOneField(Adopter, on_delete=models.CASCADE)
    # Profile Info
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Phone Number"
    )

    # Address related fields
    address_line1 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Address Line 1"
    )
    address_line2 = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Address Line 2"
    )
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="City")
    state = models.CharField(max_length=50, blank=True, null=True, verbose_name="State")
    zip_code = models.CharField(
        max_length=10, blank=True, null=True, verbose_name="ZIP Code"
    )
    country = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Country"
    )
    notes = models.TextField(
        blank=True, null=True, verbose_name="Adoption Notes or Preferences"
    )
