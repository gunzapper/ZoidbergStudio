from django.shortcuts import redirect, render

from dicom_visio.models import MDatum, Dicom

def home_page(request):
    return render(request, 'home.html')

def view_file(request):
    mdata = MDatum.objects.all()
    return render(request, 'dicom_file.html', {'mdata': mdata})

def new_dicom(request):
    dicom = Dicom.objects.create()
    MDatum.objects.create(text=request.POST['metadata_text'], dicom=dicom)
    return redirect('/dicom_visio/the-only-file-in-the-world/')
