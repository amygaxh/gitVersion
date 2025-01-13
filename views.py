from django.shortcuts import render, get_object_or_404
from .models import *

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'RrethNesh.html')

def contact(request):
    return render(request, 'Nakontaktoni.html')

def objects_list(request):
    properties = Pronat.objects.all()  
    return render(request, 'Pronat.html', {'properties': properties})

def objects_office_bllok(request):
    return render(request, 'ZyraBllok.html')

def objects_myslym_shyri(request):
    return render(request, 'KomercialMyslymShyri.html')

def objects_ekspozita(request):
    return render(request, 'KomercialEkspozita.html')

def objects_komuna(request):
    return render(request, 'ApartamentKomuna.html')

def property_detail(request, id):
    property_item = get_object_or_404(Pronat, pk=id)  
    return render(request, 'property_detail.html', {'property': property_item})
