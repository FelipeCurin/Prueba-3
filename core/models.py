from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, IntegerField

# Create your models here.
class Componente(models.Model):
    id_comp = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

    def __str__(self):
        return self.nombre

class Fabricante(models.Model):
    id_fabr = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True, blank=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def ruta_imagen(self, filename):
        return f'productos/{self.id}/{filename}'
    imagen = models.ImageField(upload_to = ruta_imagen, null=True, blank=True)
    
    def __str__(self):
        return self.nombre