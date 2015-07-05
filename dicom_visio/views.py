from django.shortcuts import redirect, render

from dicom_visio.models import MDatum

def home_page(request):
    if request.method == 'POST':
        MDatum.objects.create(text = request.POST['metadata_text'])
        return redirect('/dicom_visio/the-only-file-in-the-world/')
    return render(request, 'home.html')

def view_file(request):
    mdata = MDatum.objects.all()
    return render(request, 'dicom_file.html', {'mdata': mdata})
