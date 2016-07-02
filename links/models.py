from django.db import models


class Link(models.Model):

    name = models.CharField(max_length=80, blank=True)
    url = models.CharField(max_length=900, blank=True)
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
