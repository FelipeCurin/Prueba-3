from django.contrib import admin
from django.urls import path, include
from core.views import cpu, gpu, hdd, inicio, m2, mb, psu, ram, signin, ssd, agregar_producto
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('mb/', mb, name='mb'),
    path('cpu/', cpu, name= 'cpu'),
    path('gpu/', gpu, name= 'gpu'),
    path('ram/', ram, name= 'ram'),
    path('hdd/', hdd, name= 'hdd'),
    path('ssd/', ssd, name= 'ssd'),
    path('m2/', m2, name= 'm2'),
    path('psu/', psu, name= 'psu'),
    path('signin/', signin, name= 'signin'),
    path('agregar-producto/', agregar_producto, name="agregar_producto")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


