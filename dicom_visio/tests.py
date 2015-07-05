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

    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['metadata_text'] = 'new metadata'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],'/dicom_visio/the-only-file-in-the-world/')

    def test_home_page_only_saves_metadata_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(MDatum.objects.count(), 0)

class DicomViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/dicom_visio/the-only-file-in-the-world/')
        self.assertTemplateUsed(response, 'dicom_file.html')

    def test_displays_MData(self):
        MDatum.objects.create(text='meta datum 1')
        MDatum.objects.create(text='meta datum 2')

        response = self.client.get('/dicom_visio/the-only-file-in-the-world/')

        self.assertIn('meta datum 1', response.content.decode())
        self.assertIn('meta datum 2', response.content.decode())


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

