# post/admin.py

from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'post_thumbnail', 'created_at', 'updated_at']