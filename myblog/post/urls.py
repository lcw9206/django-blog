# post.urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post_list/$', views.post_list, name="post_list"),
    url(r'^my_post_list/$', views.my_post_list, name="my_post_list"),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name="post_detail"),
    url(r'^new/$', views.post_new, name="post_new"),
    url(r'^(?P<post_id>\d+)/delete/$', views.post_delete, name="post_delete"),
    url(r'^(?P<post_id>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^(?P<post_id>\d+)/comment/new$', views.comment_new, name="comment_new"),
    url(r'^(?P<post_id>\d+)/comment/(?P<comment_id>\d+)/delete$', views.comment_delete, name="comment_delete"),
]
