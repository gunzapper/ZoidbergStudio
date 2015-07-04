from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from dicom_visio.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func.__name__, 'home_page')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_tequest(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['metadata_text'] = 'new metadata'

        response = home_page(request)

        self.assertIn('new metadata', response.content.decode())

        expected_html = render_to_string(
            'home.html',
            {'new_metadata_text': 'new metadata'}
        )
        self.assertEqual(response.content.decode(), expected_html)
