# accounts/urls. py

from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^login/$', auth_views.login, name='login',
        kwargs={'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout',
        kwargs={'next_page': settings.LOGIN_URL}),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile_change/$', views.profile_change, name='profile_change'),

    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done',
        kwargs={'template_name': 'accounts/password_change_done.html'}),
]