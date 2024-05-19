from django.db import models
from django.conf import settings
from django.utils.text import slugify
from bs4 import BeautifulSoup
from tinymce.models import HTMLField

class BlogCategory(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Category Title")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Author"
    )
    title = models.CharField(max_length=128, verbose_name="Post Title")
    short_description = models.CharField(max_length=450, verbose_name="Short description", blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # SEO-friendly URL
    content = HTMLField()
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, verbose_name="Category"
    )
    tags = models.ManyToManyField("Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Is Published?")
    is_page = models.BooleanField(default=False, verbose_name="Is a page?")

    def clean_content_text(self):
        # Usar BeautifulSoup para limpiar el HTML
        soup = BeautifulSoup(self.content, "html.parser")
        return soup.get_text()
    def get_short_description(self, char_limit=250):
        # Obtener el contenido de texto limpio o la descripción corta
        if self.short_description:
            description = self.short_description
        else:
            description = self.clean_content_text()

        # Añadir puntos suspensivos si el contenido supera el límite
        if len(description) > char_limit:
            return description[:char_limit].rstrip() + "..."
        else:
            return description
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Blog Post",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Commenter"
    )
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False, verbose_name="Is Approved?")

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Tag Name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
