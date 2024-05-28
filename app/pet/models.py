from django.db import models
from adoption.models import Questionnaire
from shelter.models import Shelter
from django.template.defaultfilters import slugify
from django.urls import reverse


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


class PetImage(models.Model):
    image = models.ImageField(upload_to="pets/gallery/")

    class Meta:
        verbose_name = "Pet Image"
        verbose_name_plural = "Pet Images"


class Pet(models.Model):
    name = models.CharField(max_length=255, verbose_name="Pet Name")
    specie = models.ForeignKey(Specie, on_delete=models.PROTECT)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    characteristics = models.ManyToManyField(
        Characteristic,
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
    images = models.ManyToManyField(PetImage)

    slug = models.SlugField(max_length=255, null=True, verbose_name="Slug")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name + " " + self.shelter.city

    def get_absolute_url(self):
        return reverse(
            "pet",
            kwargs={
                "specie": self.specie.name,
                "city": self.shelter.city,
                "id": self.id,
                "name": self.name,
            },
        )
    
    def has_questionnaire(self):
        return Questionnaire.objects.filter(shelter=self.shelter).exists()

    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
        ordering = ["-created_at"]
