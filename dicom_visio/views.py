from django.shortcuts import redirect, render

from dicom_visio.models import MDatum, Dicom

def home_page(request):
    return render(request, 'home.html')

def view_file(request, dicom_id):
    dicom = Dicom.objects.get(id=dicom_id)
    return render(request, 'dicom.html', {'dicom':dicom})

def new_dicom(request):
    dicom = Dicom.objects.create()
    MDatum.objects.create(text=request.POST['metadata_text'], dicom=dicom)
    return redirect('/dicom_visio/%d/' % (dicom.id, ))

def add_datum(request, dicom_id):
    dicom = Dicom.objects.get(id=dicom_id)
    MDatum.objects.create(text=request.POST['metadata_text'], dicom=dicom)
    return redirect('/dicom_visio/%d/' % (dicom.id, ))
