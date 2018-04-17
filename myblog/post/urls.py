# post.urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^new/$', views.post_new, name="post_new"),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name="post_delete"),
]
