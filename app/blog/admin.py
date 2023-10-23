from django.contrib import admin
from .models import BlogCategory, BlogPost, Comment, Tag


admin.site.register(BlogCategory)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Tag)
