from django.test import TestCase

from .models import Link

import string


class LinkTest(TestCase):

    def test_link_generation(self):
        link = Link(
            name='hola',
            redirect_url='https://inventivehack.com/'
        )
        link.save()
        self.assertTrue(link.url)
