from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ProductoForm,ProveedorForm,FacturaForm,ListaProductosFacturaForm,VentaProductosFacturaForm
from .models import *
from django.contrib import messages

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



def PageVentas(request):
    # Obtener todas las facturas que tienen ventas asociadas
    facturas_con_ventas = Factura.objects.filter(venta_productos_factura__isnull=False).distinct()
        
    if request.method == 'POST':
        factura = FacturaForm(request.POST)
        if factura.is_valid():
            # guardamos el codigo de la factura
            fac = factura.save()
            # enviamos el codigo a otra vista
            return redirect('crearVentaLink',fac.codigo)
            
    facturas = Factura.objects.all()
    ventas = Venta_Productos_Factura.objects.all()
    formulario_fac = FacturaForm()
    context={
        'facturas':facturas_con_ventas,
        'form_fac':formulario_fac,
        'ventas':ventas
    }
    return render(request,"Ventas-templates/ventas.html",context)

def crearVenta(request,cod_fac):
    # todos los productos que tiene la misma factura
    lista_productos = Lista_Productos_Factura.objects.filter(codigo_factura=cod_fac)
    
    # total de la venta
    total = 0
    for producto in lista_productos:
        total += producto.producto.precio * producto.cantidad_vendida
        total=total
    
    # formulario del listado de productos con un valor inicial de el codigo de fac 
    form_listado_productos = ListaProductosFacturaForm(initial={'codigo_factura': cod_fac,'cantidad':'1'})
    # formulario de venta
    formulario_venta = VentaProductosFacturaForm(initial={'factura': cod_fac,'total':total})
    #error de stock
    error_stock = ""
    if request.method == 'POST':
         
         form = ListaProductosFacturaForm(request.POST)
         #obtenemos el codigo del producto
         cod_producto =request.POST.get('producto')
         #obtenemos el producto
         prod = Producto.objects.get(codigo=cod_producto)
         #obtenemos el stock del producto
         stock_producto = prod.stock

         cantidad = request.POST.get('cantidad_vendida')
         
         if stock_producto > int(cantidad):
            if form.is_valid():
                form.save()
                return redirect(request.path)
         else:
            error_stock = "no se puede agregar el producto por falta de stock"
             
             
    context={
        'form_listado_productos':form_listado_productos,
        'lista_productos':lista_productos,
        'formulario_venta':formulario_venta,
        'error_stock':error_stock 
    }
    return render(request,'Ventas-templates/crear-venta.html',context=context)

def procesarVenta(request,cod_fac):
    if request.method == 'POST':
        # obtenemos la lista de productos de esa factura 
        lista_productos = Lista_Productos_Factura.objects.filter(codigo_factura=cod_fac)
        # obtenemos todos los productos
        productos = Producto.objects.all()
         # quitar el stok
        for lisProd in lista_productos:
            for pro in productos:
                # preguntamos si el codigo del producto lista es el mismo que el de product
                if lisProd.producto.codigo == pro.codigo:
                   
                    # obtenemos el codigo del producto y le restamos la catidad 
                    productoObtenido = Producto.objects.get(codigo=pro.codigo)
                    # validamos el stock
                    if productoObtenido.stock > lisProd.cantidad_vendida:
                       productoObtenido.stock -= lisProd.cantidad_vendida
                       productoObtenido.save()
        
        # validacion de factura vacia   
        form = VentaProductosFacturaForm(request.POST)
        if lista_productos.exists():  #verifica si hay datos    
            if form.is_valid():
                form.save() 
                return redirect('detalleVentaLink',cod_fac)       
        else:
            # eliminamos la factura 
            Factura.objects.get(codigo=cod_fac).delete()
            # mandamos el error a una template nueva
            error = "error creaste una factura sin productos vuelve a crear una factura valida"
            return render(request,'Ventas-templates/error-venta.html',context={'error':error})
    return redirect('PageVentasLink')

def eliminarProductoLista(request,cod_prod_list):
    producto_lista = Lista_Productos_Factura.objects.get(codigo=cod_prod_list).delete()
    url_pagina_anterior = request.META.get('HTTP_REFERER')

    # Redireccionar a la página anterior
    return redirect(url_pagina_anterior)


def eliminarVenta(request,cod_fac):
    factura = Factura.objects.get(codigo=cod_fac).delete()
    return redirect('PageVentasLink') 

def detalleVenta(request,cod_fac):
    factura =Factura.objects.get(codigo=cod_fac)
    lista = Lista_Productos_Factura.objects.filter(codigo_factura=cod_fac)
    venta = Venta_Productos_Factura.objects.get(factura=cod_fac)
    titulo = f"Tiket {factura}"
    lugar = "Puente Piedra"
    telefono = '52345432532'
    fecha_for = "12/12/12"
    
    context = {
        'factura':factura,
        'lista_productos':lista,
        'venta':venta,
        'titulo':titulo,
        'lugar':lugar,
        'telefono':telefono,
        "fechaFor":fecha_for
    }
    return render(request,'Ventas-templates/detalle-venta.html',context)

from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(request, titulo, fecha, lugar, metodo_pago, codigo):
    
    # Crear el contenido del PDF
    pdf_content = []
    pdf_content.append(Paragraph(titulo, getSampleStyleSheet()['Title']))
    pdf_content.append(Paragraph(f"Fecha y Hora: {fecha}", getSampleStyleSheet()['BodyText']))
    pdf_content.append(Paragraph(f"Lugar: {lugar}", getSampleStyleSheet()['BodyText']))
    pdf_content.append(Paragraph(f"Método de Pago: {metodo_pago}", getSampleStyleSheet()['BodyText']))
    pdf_content.append(Paragraph(f"Código: {codigo}", getSampleStyleSheet()['BodyText']))

    lista = Lista_Productos_Factura.objects.filter(codigo_factura=codigo)
    # venta = Venta_Productos_Factura.objects.get(factura=codigo)
    data = [["Producto", "Precio unitario", "Cantidad", "Total"]]
    total = 0
    for lis in lista:
        subtotal = lis.producto.precio * lis.cantidad_vendida
        total += subtotal
        data.append([lis.producto, f"${lis.producto.precio}", str(lis.cantidad_vendida), f"${subtotal}"])
    # for product in productos:
    #     subtotal = product["precio"] * product["cantidad"]
    #     total += subtotal
    #     data.append([product["nombre"], f"${product['precio']}", str(product["cantidad"]), f"${subtotal}"])

    table = Table(data)
    style = TableStyle([('TEXTCOLOR', (0, 0), (-1, -1), (0, 0, 0)),  # Color de texto: negro
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])  # Color de la línea de la tabla: negro
    table.setStyle(style)
    pdf_content.append(table)

    pdf_content.append(Paragraph(f"Total de Productos: {len(lista)}", getSampleStyleSheet()['BodyText']))
    pdf_content.append(Paragraph(f"Total: ${total}", getSampleStyleSheet()['BodyText']))

    # Generar el PDF
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    pdf.build(pdf_content)

    # Devolver el PDF como respuesta HTTP
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ticket_venta.pdf"'
    response.write(buffer.getvalue())
    buffer.close()
    return response



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



#LOGIN

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy


# Decorador para restringir el acceso a vistas solo para administradores
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.username == 'Admin1':
            return view_func(request, *args, **kwargs)
        elif request.user.is_authenticated and request.user.username == 'Vendedor':
            return redirect(reverse_lazy('PageVentasLink'))  # Redirige a la página de ventas si el usuario es un vendedor
        else:
            return redirect('login')  # Redirige a la página de inicio de sesión si no está autenticado como Admin
    return wrapper

# Decorador para restringir el acceso a vistas solo para vendedores
def vendor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.username == 'Vendedor':
            return view_func(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('PageVentasLink'))  # Redirige a la página de ventas si no está autenticado como Vendedor
    return wrapper

# Aplica los decoradores a tus vistas

@login_required
def PageInicio(request):
    # Esta vista puede ser accedida tanto por Admin como por Vendedor
    return render(request, "inicio.html")

@login_required
@admin_required
def PageProductos(request):
    # Esta vista está restringida solo para Admin y Vendedor
    productos = Producto.objects.all()
    form = ProductoForm()
    context = {
        'productos': productos,
        'formulario': form,
    }
    return render(request, "Productos-templates/productos.html", context)

@login_required
def PageVentas(request):
    # Esta vista puede ser accedida por Admin y Vendedor
    if request.method == 'POST':
        factura = FacturaForm(request.POST)
        if factura.is_valid():
            # Guardamos el código de la factura
            fac = factura.save()
            # Enviamos el código a otra vista
            return redirect('crearVentaLink', fac.codigo)

    facturas = Factura.objects.all()
    formulario_fac = FacturaForm()
    context = {
        'facturas': facturas,
        'form_fac': formulario_fac,
    }
    return render(request, "Ventas-templates/ventas.html", context)

# Aplica decoradores similares a otras vistas según sea necesario
