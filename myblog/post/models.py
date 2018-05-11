# post/models.py

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
import datetime


def set_post_path(instance, filename):
    now = datetime.datetime.now()

    path = 'images/post/{username}/{year}_{month}_{day}/{micro}.{extension}'.format(
        username=instance.user.username,
        year=now.year,
        month=now.month,
        day=now.day,
        micro=now.microsecond,
        extension=filename.split('.')[-1]
    )
    return path


class Category(models.Model):
    name = models.CharField("카테고리명", max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('POST', related_name='comments')
    content = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_thumbnail = ProcessedImageField(
        verbose_name='사진',
        upload_to=set_post_path,
        processors=[Thumbnail(262, 262)],
        format='JPEG',
        options={'quality': 60},
        blank=True
    )
    title = models.CharField(max_length=40, verbose_name='제목')
    content = models.CharField(max_length=150, verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일자')
    category = models.ForeignKey(Category, null=False, verbose_name='카테고리')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.id])
