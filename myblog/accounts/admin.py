# accounts/admin.py

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['id', 'user_id', 'about', 'profile_thumbnail']
    list_select_related = ['user']

