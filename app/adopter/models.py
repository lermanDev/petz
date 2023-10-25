from django.db import models
from django.contrib.auth.models import AbstractUser

from pet.models import Specie, Size, Pet


class Adopter(AbstractUser):
    # Profile Info
    full_name = models.CharField(max_length=255, verbose_name="Full Name")
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Phone Number"
    )

    # Preferences for adoptions
    preferred_pet_size = models.ForeignKey(
        Size, blank=True, null=True, on_delete=models.PROTECT
    )
    preferred_species = models.ManyToManyField(
        Specie, blank=True, null=True, verbose_name="Preferred Species"
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

    # Record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    # Django required fields
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="adopter_set",
        related_query_name="adopter",
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="adopter_set",
        related_query_name="adopter",
        verbose_name="user permissions",
    )

    class Meta:
        verbose_name = "Adopter"
        verbose_name_plural = "Adopters"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name or self.username
