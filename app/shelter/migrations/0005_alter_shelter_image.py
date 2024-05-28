# Generated by Django 4.2.13 on 2024-05-28 01:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shelter", "0004_state_alter_shelter_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shelter",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="shelters/gallery/",
                verbose_name="Principal Image",
            ),
        ),
    ]
