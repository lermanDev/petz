from django.db import models
from pet.models import Pet
from adopter.models import Adopter


class Adoption(models.Model):
    ADOPTION_STATUS_CHOICES = [
        ("ready", "Ready"),
        ("special_condition", "Special Condition"),
        ("reserved", "Reserved"),
        ("waiting", "Waiting"),
        ("adopted", "Adopted"),
        ("deleted", "Deleted"),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name="Pet")
    status = models.CharField(
        max_length=20, choices=ADOPTION_STATUS_CHOICES, verbose_name="Adoption Status"
    )
    extra_location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Extra Location"
    )
    entry_date = models.DateTimeField(verbose_name="Entry Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    history = models.TextField(blank=True, null=True, verbose_name="History")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Adoption"
        verbose_name_plural = "Adoptions"


class AdoptionRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]

    adoption = models.ForeignKey(
        Adoption, on_delete=models.CASCADE, verbose_name="Adoption"
    )
    adopter = models.ForeignKey(
        Adopter, on_delete=models.CASCADE, verbose_name="Adopter"
    )
    status = models.CharField(
        max_length=20,
        choices=REQUEST_STATUS_CHOICES,
        default="pending",
        verbose_name="Request Status",
    )

    message = models.TextField(blank=True, null=True, verbose_name="Message to Shelter")
    response = models.TextField(
        blank=True, null=True, verbose_name="Response from Shelter"
    )

    # Record keeping
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Adoption Request"
        verbose_name_plural = "Adoption Requests"
