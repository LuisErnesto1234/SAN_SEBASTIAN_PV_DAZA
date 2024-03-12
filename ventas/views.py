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

def PageProductosCategorias(request):
    categorias = Categoria.objects.all()
    contex={
        'categorias':categorias,
    }
    return render(request,"productos_categorias.html",contex)

def PageProductosMarcas(request):
    marcas = Marca.objects.all()
    contex={
        'marcas':marcas,
    }
    return render(request,"productos_marcas.html",contex)

def PageProductosProveedores(request):
    proveedores = Proveedor.objects.all()
    contex={
        'proveedores':proveedores,
    }
    return render(request,"productos_proveedores.html",contex)
