from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from links import urls as link_urls

admin_url = r'^{}/'.format(settings.ADMIN_URL)
default_redirect_url = settings.DEFAULT_REDIRECT_URL

urlpatterns = [
    url(admin_url, include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=default_redirect_url)),
    url('', include(link_urls, namespace='links'))
]
