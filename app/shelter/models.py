from django.db import models


class Shelter(models.Model):
    name = models.CharField(max_length=255, verbose_name="Shelter Name")
    address = models.TextField(verbose_name="Address")
    city = models.CharField(max_length=100, verbose_name="City")
    state = models.CharField(max_length=100, verbose_name="State")
    zip_code = models.CharField(max_length=10, verbose_name="Zip Code")
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Phone Number"
    )
    email = models.EmailField(null=True, blank=True, verbose_name="Email Address")
    website = models.URLField(null=True, blank=True, verbose_name="Website")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    image = models.ImageField(
        upload_to="static/shelters/gallery/",
        null=True,
        blank=True,
        verbose_name="Principal Image",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shelter"
        verbose_name_plural = "Shelters"
        ordering = ["name"]
