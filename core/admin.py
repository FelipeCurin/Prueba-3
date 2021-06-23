from django.contrib import admin
from .models import Componente, Fabricante, Producto 
# Register your models here.

admin.site.register(Componente)
admin.site.register(Fabricante)
admin.site.register(Producto)