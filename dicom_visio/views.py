from django.shortcuts import redirect, render

from dicom_visio.models import MDatum

def home_page(request):
    if request.method == 'POST':
        MDatum.objects.create(text = request.POST['metadata_text'])
        return redirect('/')

    mdata = MDatum.objects.all()
    return render(request, 'home.html', {'mdata': mdata})
