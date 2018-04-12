# myblog/urls.py

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^post/', include('post.urls')),
]


urlpatterns += static('media/', document_root=settings.MEDIA_ROOT)
