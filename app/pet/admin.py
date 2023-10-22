from django.contrib import admin
from .models import Pet, PetImage, Specie, Size, Gender, Characteristic


admin.site.register(Pet)
admin.site.register(PetImage)
admin.site.register(Specie)
admin.site.register(Size)
admin.site.register(Gender)
admin.site.register(Characteristic)
