# accounts/models.py

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
import datetime


def set_image_path(instance, filename):
    now = datetime.datetime.now()

    path = "images/{username}/{year}_{month}_{day}/{micro}.{extension}".format(
        username=instance.user.username,
        year=now.year,
        month=now.month,
        day=now.day,
        micro=now.microsecond,
        extension= filename.split('.')[-1]
    )
    return path


# User 생성 시, Queryset과 signals를 이용해 Profile 데이터 자동 생성
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    about = models.CharField(max_length=100)
    photo_thumbnail = ProcessedImageField(
        upload_to=set_image_path,
        default='myblog/static/avatar.jpeg',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 60},
        blank=True
    )

    def get_user(self):
        return User.objects.get(pk=self.user)




