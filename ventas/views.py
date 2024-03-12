from django.shortcuts import render
from .models import *

# Create your views here.

def PageInicio(request):
    return render(request,"inicio.html")


def PageProductos(request):
    productos = Producto.objects.all()
    
    contex={
        'productos':productos,
    }
    
    return render(request,"productos.html",contex)
