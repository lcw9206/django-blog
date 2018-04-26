# post.urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^new/$', views.post_new, name="post_new"),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name="post_delete"),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^(?P<id>\d+)/comment/new$', views.comment_new, name="comment_new"),
]
