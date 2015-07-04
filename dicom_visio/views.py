from django.http import HttpResponse
from django.shortcuts import render

from dicom_visio.models import MDatum

def home_page(request):
    mdatum = MDatum()
    mdatum.text = request.POST.get('metadata_text', '')
    mdatum.save()

    return render(request, 'home.html',{
            'new_metadata_text': mdatum.text,  
        })
