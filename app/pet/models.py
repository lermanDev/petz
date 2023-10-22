from django.db import models
from shelter.models import Shelter


class Specie(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Species Name")
    description = models.TextField(null=True, blank=True, verbose_name="Description")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Specie"
        verbose_name_plural = "Species"
        ordering = ["name"]


class Characteristic(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Characteristic Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Characteristic"
        verbose_name_plural = "Characteristics"
        ordering = ["name"]


class Gender(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Gender")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"
        ordering = ["name"]


class Size(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Size")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"
        ordering = ["name"]


class Pet(models.Model):
    name = models.CharField(max_length=255, verbose_name="Pet Name")
    specie = models.ForeignKey(Specie, on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    characteristics = models.ManyToManyField(
        Characteristic,
        blank=True,
        related_name="pets",
        verbose_name="List of Characteristics",
    )
    health = models.CharField(max_length=255, verbose_name="Health Description")
    description = models.CharField(max_length=255, verbose_name="Pet Description")
    shelter = models.ForeignKey(
        Shelter, on_delete=models.CASCADE, related_name="pets", verbose_name="Shelter"
    )
    weight = models.FloatField(verbose_name="Weight")
    birth_date = models.DateTimeField(verbose_name="Birth Date")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ["-created_at"]


class PetImage(models.Model):
    pet = models.ForeignKey(Pet, related_name="petimages", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pets/gallery/")

    class Meta:
        verbose_name = "Pet Image"
        verbose_name_plural = "Pet Images"
