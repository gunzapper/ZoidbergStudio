from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html',{
            'new_metadata_text': request.POST.get('metadata_text', ''),
            })
