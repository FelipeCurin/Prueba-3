from core.models import Producto
from .models import Producto
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import ProductoForm
# Create your views here.
    
def inicio(request):

    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'Inicio.html', data)

def mb(request):
    return render(request, 'mb.html',{})

def cpu(request):
    return render(request, 'Cpu.html',{})

def gpu(request):
    return render(request, 'Gpu.html',{})

def hdd(request):
    return render(request, 'Hdd.html',{})

def m2(request):
    return render(request, 'M2.html',{})

def psu(request):
    return render(request, 'Psu.html',{})

def ram(request):
    return render(request, 'Ram.html',{})

def ssd(request):
    return render(request, 'Ssd.html',{})

def signin(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            username = {"Nombre":'username'}
            return render(request, 'Inicio.html', {username})
        else:
            return render(request, 'Signin.html')

def agregar_producto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'Administrador.html', data)