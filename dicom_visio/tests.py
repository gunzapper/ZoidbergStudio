from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from dicom_visio.views import home_page
from dicom_visio.models import MDatum

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func.__name__, 'home_page')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['metadata_text'] = 'new metadata'

        response = home_page(request)

        self.assertEqual(MDatum.objects.count(), 1)

        new_mdatum = MDatum.objects.first()
        self.assertEqual(new_mdatum.text, 'new metadata')

        self.assertIn('new metadata', response.content.decode())

        expected_html = render_to_string(
            'home.html',
            {'new_metadata_text': 'new metadata'}
        )
        self.assertEqual(response.content.decode(), expected_html)

# Integrated tests

# Note: think here how to update also
# metadata in dicom files.
# Note: In the database we have to store
# also the path of the file (or more weird the image)
class MDatumModelTest(TestCase):
    # In a first moment metadata
    # are a stand alone text
    def test_saving_and_retrieving_metadata(self):
        first_mdatum = MDatum()
        first_mdatum.text = "The first (ever) dicom meta datum"
        first_mdatum.save()

        second_mdatum = MDatum()
        second_mdatum.text = "Another meta datum"
        second_mdatum.save()

        saved_mdata = MDatum.objects.all()
        self.assertEqual(saved_mdata.count(), 2)
        self.assertEqual(saved_mdata[0].text,"The first (ever) dicom meta datum")
        self.assertEqual(saved_mdata[1].text, "Another meta datum")

