from django.db import models
from pet.models import Pet
from shelter.models import Shelter
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
    user = models.ForeignKey(
        Adopter,
        on_delete=models.CASCADE,
        related_name="adoptions_made",
        verbose_name="Adopter",
    )
    shelter = models.ForeignKey(
        Shelter, on_delete=models.CASCADE, verbose_name="Shelter"
    )
    adopted_by = models.ForeignKey(
        Adopter,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="adoptions_received",
        verbose_name="Adopted By",
    )
    status = models.CharField(
        max_length=20, choices=ADOPTION_STATUS_CHOICES, verbose_name="Adoption Status"
    )
    extra_location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Extra Location"
    )
    entry_date = models.DateTimeField(verbose_name="Entry Date")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Adoption"
        verbose_name_plural = "Adoptions"
