# accounts/models.py

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)



