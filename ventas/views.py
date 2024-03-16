from django.shortcuts import render,redirect
from .forms import ProductoForm,ProveedorForm
from .models import *

######  PAGINAS DE PRINSIPALES  ######

def PageInicio(request):
    return render(request,"inicio.html")

def PageProductos(request):
    productos = Producto.objects.all()
    form = ProductoForm()
    contex={
        'productos':productos,
        'formulario':form,
    }
    return render(request,"productos.html",contex)

######  PAGINAS RELACIONADAS A PRODUCTOS  ######
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
    form = ProveedorForm()
    contex={
        'proveedores':proveedores,
        'formulario':form,
    }
    return render(request,"productos_proveedores.html",contex)

# crear
def crearProducto(request):
    producto = ProductoForm(request.POST,request.FILES)
    if producto.is_valid():
        producto.save()
        return redirect('PageProductosLink')
    else :
       return render(request,'estadisticas.html')

def crearCategoria(request):
    if request.method == 'POST':
        dato1 = request.POST.get('int-codigo')
        dato2 = request.POST.get('txt-nombre')
        Categoria.objects.create(codigo_categoria=dato1,nombre_categoria=dato2)
        return redirect('PageProductosCategoriasLink')
    else:
        return render(request,'estadisticas.html')

def crearMarca(request):
    if request.method == 'POST':
        dato1 = request.POST.get('int-codigo')
        dato2 = request.POST.get('txt-nombre')
        Marca.objects.create(codigo_marca=dato1,nombre_marca=dato2)
        return redirect('PageProductosMarcasLink')
    else:
        return render(request,'estadisticas.html')
def crearProveedor(request):
    proveedor = ProveedorForm(request.POST)
    if proveedor.is_valid():
        proveedor.save()
        return redirect('PageProductosProveedoresLink')
    else :
       return render(request,'estadisticas.html')

# editar
def editarProducto(request,id):
    pass
def editarCategoria(request,id):
    pass
def editarMarca(request,id):
    pass
def editarProveedor(request,id):
    pass
# eliminar
def eliminarProducto(request,id):
    pass
def eliminarCategoria(request,id):
    pass
def eliminarMarca(request,id):
    pass
def eliminarProveedor(request,id):
    pass
# detalles
def detalleProducto(request,id):
    pass

