# Generated by Django 4.2.13 on 2024-05-18 12:52

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogpost_is_page_blogpost_short_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=tinymce.models.HTMLField(),
        ),
    ]
