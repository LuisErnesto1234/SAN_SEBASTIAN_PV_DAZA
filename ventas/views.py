from django.shortcuts import render,redirect
from .forms import ProductoForm,ProveedorForm,ProductoVendidoForm
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
    return render(request,"Productos-templates/productos.html",contex)

######  PAGINAS RELACIONADAS A PRODUCTOS  ######
def PageProductosCategorias(request):
    categorias = Categoria.objects.all()
    contex={
        'categorias':categorias,
    }
    return render(request,"Productos-templates/productos_categorias.html",contex)

def PageProductosMarcas(request):
    marcas = Marca.objects.all()
    contex={
        'marcas':marcas,
    }
    return render(request,"Productos-templates/productos_marcas.html",contex)

def PageProductosProveedores(request):
    proveedores = Proveedor.objects.all()
    form = ProveedorForm()
    contex={
        'proveedores':proveedores,
        'formulario':form,
    }
    return render(request,"Productos-templates/productos_proveedores.html",contex)

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
def editarProducto(request,codigo_producto):
    producto = Producto.objects.get(codigo=codigo_producto)
    formulario = ProductoForm(instance=producto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST ,request.FILES,instance=producto) 
        if form.is_valid():
            form.save()
            return redirect('PageProductosLink') 
    context={
        'producto':producto,
        'formulario':formulario,
        }
    return render(request,'Productos-templates/productos-editar.html',context=context)

def editarCategoria(request,codigo_categoria):
    categoria = Categoria.objects.get(codigo=codigo_categoria)
    if request.method == 'POST':
        dato1 = request.POST.get('int-codigo')
        dato2 = request.POST.get('txt-nombre')
        Categoria.objects.filter(codigo=categoria.codigo).update(codigo_categoria=dato1,nombre_categoria=dato2)

        return redirect('PageProductosCategoriasLink')
    context={
        'categoria':categoria,
    }
    return render(request,'Productos-templates/producto_categorias-editar.html',context)

def editarMarca(request,codigo_marca):
    marca = Marca.objects.get(codigo=codigo_marca)
    if request.method == 'POST':
        dato1 = request.POST.get('int-codigo')
        dato2 = request.POST.get('txt-nombre')
        Marca.objects.filter(codigo=marca.codigo).update(codigo_marca=dato1,nombre_marca=dato2)

        return redirect('PageProductosMarcasLink')
    context={
        'marca':marca,
    }
    return render(request,'Productos-templates/producto_marcas-editar.html',context)

def editarProveedor(request,codigo_proveedor):
    proveedor = Proveedor.objects.get(codigo=codigo_proveedor)
    formulario = ProveedorForm(instance=proveedor)
    
    if request.method == 'POST':
        form = ProveedorForm(request.POST,instance=proveedor) 
        if form.is_valid():
            form.save()
            return redirect('PageProductosProveedoresLink') 
    context={
        'proveedor':proveedor,
        'formulario':formulario,
        }
    return render(request,'Productos-templates/producto_proveedor-editar.html',context=context)

# eliminar
def eliminarProducto(request,codigo_producto):
    Producto.objects.get(codigo=codigo_producto).delete()
    return redirect('PageProductosLink')

def eliminarCategoria(request,codigo_categoria):
    Categoria.objects.get(codigo=codigo_categoria).delete()
    return redirect('PageProductosCategoriasLink')
    
def eliminarMarca(request,codigo_marca):
    Marca.objects.get(codigo=codigo_marca).delete()
    return redirect('PageProductosMarcasLink')

def eliminarProveedor(request,codigo_proveedor):
    Proveedor.objects.get(codigo=codigo_proveedor).delete()
    return redirect('PageProductosProveedoresLink')

# detalles
def detalleProducto(request,codigo_producto):
    producto =  Producto.objects.get(codigo=codigo_producto)
    return render(request,'Productos-templates/producto_detalles.html',context={
        'producto':producto
    })



<<<<<<< HEAD

def PageVentas(request):
    facturas = Factura.objects.all()

    context={
        'facturas':facturas,
    }
    return render(request,"Ventas-templates/ventas.html",context)


def crearVenta(request):
    formulario = ProductoVendidoForm()
    context={
        'formulario':formulario
    }
    return render(request,'Ventas-templates/crear-venta.html',context=context)
=======
# Imprimir excel de productos

from django.http import HttpResponse
from openpyxl import Workbook

def descargar_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="productos.xlsx"'

    # Crear un nuevo libro de trabajo de Excel
    wb = Workbook()
    # Obtener la hoja de cálculo activa
    ws = wb.active

    # Agregar encabezados
    ws.append(['Código Producto', 'Código Barras', 'Nombre', 'Precio', 'Stock', 'Categoría', 'Marca', 'Proveedor'])

    # Agregar datos de productos
    productos = Producto.objects.all()
    for producto in productos:
        ws.append([producto.codigo_producto, producto.codigo_barras, producto.nombre, producto.precio, producto.stock, producto.categoria.nombre_categoria, producto.marca.nombre_marca, producto.proveedor.nombres])

    # Guardar el libro de trabajo
    wb.save(response)

    return response

# Imprimir excel de categoria
def descargar_excel_categoria(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Categorias.xlsx"'

    # Crear un nuevo libro de trabajo de Excel
    wb = Workbook()
    # Obtener la hoja de cálculo activa
    ws = wb.active

    # Agregar encabezados
    ws.append(['Código', 'Nombre'])

    # Agregar datos de categorías
    categorias = Categoria.objects.all()
    for categoria in categorias:
        ws.append([categoria.codigo_categoria, categoria.nombre_categoria])

    # Guardar el libro de trabajo
    wb.save(response)

    return response

# Imprimir excel de Marcas
def descargar_excel_marca(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Marca.xlsx"'

    # Crear un nuevo libro de trabajo de Excel
    wb = Workbook()
    # Obtener la hoja de cálculo activa
    ws = wb.active

    # Agregar encabezados
    ws.append(['Código', 'Nombre'])

    # Agregar datos de marcas
    marcas = Marca.objects.all()
    for marca in marcas:
        ws.append([marca.codigo_marca, marca.nombre_marca])

    # Guardar el libro de trabajo
    wb.save(response)

    return response

# Imprimir excel de Proveedores
def descargar_excel_proveedores(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Proveedores.xlsx"'

    # Crear un nuevo libro de trabajo de Excel
    wb = Workbook()
    # Obtener la hoja de cálculo activa
    ws = wb.active

    # Agregar encabezados
    ws.append(['Código de Proveedor', 'Nombres', 'Apellidos', 'RUC/DNI', 'Dirección', 'Correo Electrónico', 'Número de Teléfono'])

    # Agregar datos de proveedores
    proveedores = Proveedor.objects.all()
    for proveedor in proveedores:
        ws.append([proveedor.codigo_proveedor, proveedor.nombres, proveedor.apellidos, proveedor.ruc_dni, proveedor.direccion, proveedor.correo_electronico, proveedor.numero_telefono])

    # Guardar el libro de trabajo
    wb.save(response)

    return response
>>>>>>> 7b86026d9085d7202b8d6892847a09eadb705df2
