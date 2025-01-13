from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
    path('Rreth Nesh/', views.about, name='RrethNesh'),  
    path('Na Kontaktoni/', views.contact, name='Nakontaktoni'),  
    path('Pronat/', views.objects_list, name='Pronat'),  
    path('Pronat/Zyra Bllok/', views.objects_office_bllok, name='Zyra Bllok'), 
    path('Pronat/Komercial Myslym-Shyri/', views.objects_myslym_shyri, name='Komercial Myslym Shyri'),  
    path('Pronat/Komercial Ekspozita/', views.objects_ekspozita, name='Komercial Ekspozita'),  
    path('Pronat/Apartament Komuna/', views.objects_komuna, name='Apartament Komuna'),  
    path('Pronat/<int:id>/', views.property_detail, name='PropertyDetail'),  
]
