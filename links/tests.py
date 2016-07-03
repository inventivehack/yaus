from django.test import (
    Client,
    TestCase
)

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

    def test_link_redirection(self):
        link = Link(
            name="Inventive's Facebook fan page.",
            url='fb',
            redirect_url='https://facebook.com/inventivehack/'
        )
        link.save()

        c = Client()
        response = c.get('/{}/'.format(link.url))
        self.assertEqual(response.status_code, 302)

        link = Link.objects.get(url='fb')
        self.assertEqual(link.hits, 1)

    def test_wrong_link(self):
        c = Client()
        response = c.get('/hello-world/')
        self.assertEqual(response.status_code, 404)