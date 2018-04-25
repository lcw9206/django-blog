# accounts/models.py

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
import datetime


def set_profile_path(instance, filename):
    now = datetime.datetime.now()

    path = "images/profile/{username}/{year}_{month}_{day}/{micro}.{extension}".format(
        username=instance.user.username,
        year=now.year,
        month=now.month,
        day=now.day,
        micro=now.microsecond,
        extension= filename.split('.')[-1]
    )
    return path


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.CharField(max_length=100, blank=True, verbose_name='자기소개')
    profile_thumbnail = ProcessedImageField(
        verbose_name='프로필 사진',
        upload_to=set_profile_path,
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 60},
        blank=True,
    )

    def get_user(self):
        return User.objects.get(pk=self.user)

    def __str__(self):
        return self.user
