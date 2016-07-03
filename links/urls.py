from django.conf.urls import url

from .views import (
    URLRedirectView
)

urlpatterns = [

    url(r'^(?P<url>[-\w]+)/$', URLRedirectView.as_view(), name='redirect'),

]
