from django.db import models

from .utils import gen_url


class Link(models.Model):

    name = models.CharField(max_length=80, blank=True)
    url = models.CharField(max_length=900, blank=True, unique=True)
    redirect_url = models.URLField()

    hits = models.IntegerField(default=0)

    # Metadata
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'

    def save(self, *args, **kwargs):
        if not self.url:
            repeated = 0
            length = 6
            while repeated >= 0:
                url = gen_url(length=length)
                q = Link.objects.filter(url=url)
                if q:
                    repeated += 1
                else:
                    repeated = -1
                if repeated >= 10:
                    length += 1
            self.url = url
        return super(Link, self).save(*args, **kwargs)
