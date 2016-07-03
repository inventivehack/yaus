from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from .models import Link


class URLRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = get_object_or_404(Link, url=kwargs.get('url', None))
        url.hits += 1
        url.save()
        return url.redirect_url
