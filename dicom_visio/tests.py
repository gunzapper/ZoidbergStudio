from django.core.urlresolvers import resolve
from django.test import TestCase
from dicom_visio.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func.__name__, 'home_page')
