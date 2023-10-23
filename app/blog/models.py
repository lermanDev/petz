from django.db import models
from django.conf import settings
from django.utils.text import slugify


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
    title = models.CharField(max_length=255, verbose_name="Post Title")
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # SEO-friendly URL
    content = models.TextField(verbose_name="Content")
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, verbose_name="Category"
    )
    tags = models.ManyToManyField("Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Is Published?")

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
