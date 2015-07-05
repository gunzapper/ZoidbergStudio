from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from dicom_visio.views import home_page
from dicom_visio.models import MDatum, Dicom

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')

        self.assertEqual(found.func.__name__, 'home_page')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class DicomViewTest(TestCase):
    # this part is going to be changed
    # I need not to create a new dicom
    # may be a new user

    def test_saving_a_POST_request(self):
        self.client.post(
                '/dicom_visio/new',
                data={'metadata_text': 'new metadata'}
        )

        self.assertEqual(MDatum.objects.count(), 1)

        new_mdatum = MDatum.objects.first()
        self.assertEqual(new_mdatum.text, 'new metadata')

    def test_redirects_after_POST(self):
        response =  self.client.post(
               '/dicom_visio/new',
                data={'metadata_text': 'new metadata'}
        )
        new_dicom = Dicom.objects.first()
        self.assertRedirects(response, '/dicom_visio/%d/' % (new_dicom.id))

    def test_uses_dicom_template(self):
        dicom = Dicom.objects.create()
        response = self.client.get('/dicom_visio/%d/' %(dicom.id,))
        self.assertTemplateUsed(response, 'dicom.html')

    def test_displays_metadata_from_that_dicom(self):
        correct_dicom = Dicom.objects.create()
        MDatum.objects.create(text='meta datum 1', dicom=correct_dicom)
        MDatum.objects.create(text='meta datum 2', dicom=correct_dicom)
        other_dicom = Dicom.objects.create()
        MDatum.objects.create(text='other dicom datum 1', dicom=other_dicom)
        MDatum.objects.create(text='other dicom datum 2', dicom=other_dicom)

        response = self.client.get('/dicom_visio/%d/' % (correct_dicom.id,))

        self.assertContains(response, 'meta datum 1')
        self.assertContains(response, 'meta datum 2')
        self.assertNotContains(response, 'other dicom datum 1')
        self.assertNotContains(response, 'other dicom datum 2')

# Integrated tests

# Note: think here how to update also
# metadata in dicom files.
# Note: In the database we have to store
# also the path of the file (or more weird the image)
class DicomAndMDatumModelTest(TestCase):
    # In a first moment metadata
    # are a stand alone text
    def test_saving_and_retrieving_metadata(self):
        dicom = Dicom()
        dicom.save()

        first_mdatum = MDatum()
        first_mdatum.text = "The first (ever) dicom meta datum"
        first_mdatum.dicom = dicom
        first_mdatum.save()

        second_mdatum = MDatum()
        second_mdatum.text = "Another meta datum"
        second_mdatum.dicom = dicom
        second_mdatum.save()

        saved_dicom = Dicom.objects.first()
        self.assertEqual(saved_dicom, dicom)

        saved_mdata = MDatum.objects.all()
        self.assertEqual(saved_mdata.count(), 2)

        self.assertEqual(saved_mdata[0].text,"The first (ever) dicom meta datum")
        self.assertEqual(saved_mdata[0].dicom, dicom)
        self.assertEqual(saved_mdata[1].text, "Another meta datum")
        self.assertEqual(saved_mdata[1].dicom, dicom)

