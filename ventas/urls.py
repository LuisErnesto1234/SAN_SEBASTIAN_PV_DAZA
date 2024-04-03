from django.urls import path,include
from . import views


from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .views import admin_required
from django.contrib.auth.views import logout_then_login
#PROBANDO PULL REQUEST
#PROBANDO PULL REQUEST2
#PROBANDO PULL REQUEST2 3 desde el usuario admin

urlpatterns = [
    path('', LoginView.as_view(template_name='Login.html'), name='login'),
    path('PaginaInicio/', login_required(views.PageInicio), name="PageInicioLink"),
    # SECCION DE VENTAS
    path('ventas/', login_required(views.PageVentas), name="PageVentasLink"),
    path('crear-ventas/<int:cod_fac>/', login_required(views.crearVenta), name="crearVentaLink"),
    path('procesar-ventas/<int:cod_fac>/', login_required(views.procesarVenta), name="procesarVentaLink"),
    path('ventas',views.PageVentas,name="PageVentasLink"),
    path('crear-ventas/<int:cod_fac>',login_required(views.crearVenta),name="crearVentaLink"),
    path('procesar-ventas/<int:cod_fac>',login_required(views.procesarVenta),name="procesarVentaLink"),
    path('eliminar-producto-lista/<int:cod_prod_list>',login_required(views.eliminarProductoLista),name="eliminarProductoListaLink"),
    path('eliminar-ventas/<int:cod_fac>',login_required(views.eliminarVenta),name="eliminarVentaLink"),
    path('detalle-venta/<int:cod_fac>',login_required(views.detalleVenta),name='detalleVentaLink'),
    path('generar_pdf/<str:titulo>/<str:fecha>/<str:lugar>/<str:metodo_pago>/<str:codigo>/', login_required(views.generate_pdf), name='generar_pdf'),
    # SECCION DE PRODUCTOS
    path('productos/', admin_required(views.PageProductos), name="PageProductosLink"),
    path('productos-Categorias/', admin_required(views.PageProductosCategorias), name="PageProductosCategoriasLink"),
    path('productos-Marcas/', admin_required(views.PageProductosMarcas), name="PageProductosMarcasLink"),
    path('productos-Proveedores/', admin_required(views.PageProductosProveedores), name="PageProductosProveedoresLink"),
    # CRUD DE PRODUCTOS
    path('crear-producto/', admin_required(views.crearProducto), name="crearProductosLink"),
    path('editar-producto/<int:codigo_producto>/', admin_required(views.editarProducto), name="editarProductoLink"),
    path('eliminar-producto/<int:codigo_producto>/', admin_required(views.eliminarProducto), name="eliminarProductoLink"),
    path('detalle-producto/<int:codigo_producto>/', admin_required(views.detalleProducto), name="detalleProductoLink"),
    # CRUD DE CATEGORIAS
    path('crear-categoria/', admin_required(views.crearCategoria), name="crearCategoriaLink"),
    path('editar-categoria/<int:codigo_categoria>/', admin_required(views.editarCategoria), name="editarCategoriaLink"),
    path('eliminar-categoria/<int:codigo_categoria>/', admin_required(views.eliminarCategoria), name="eliminarCategoriaLink"),
    # CRUD DE MARCA
    path('crear-marca/', admin_required(views.crearMarca), name="crearMarcaLink"),
    path('editar-marca/<int:codigo_marca>/', admin_required(views.editarMarca), name="editarMarcaLink"),
    path('eliminar-marca/<int:codigo_marca>/', admin_required(views.eliminarMarca), name="eliminarMarcaLink"),
    # CRUD DE PROVEEDOR
    path('crear-proveedor/', admin_required(views.crearProveedor), name="crearProveedorink"),
    path('editar-proveedor/<int:codigo_proveedor>/', admin_required(views.editarProveedor), name="editarProveedorLink"),
    path('eliminar-proveedor/<int:codigo_proveedor>/', admin_required(views.eliminarProveedor), name="eliminarProveedorLink"),
    # Descargar mi csv
    path('descargar-excel/', admin_required(views.descargar_excel), name='descargar_excel'),
    path('descargar-excel-categoria/', admin_required(views.descargar_excel_categoria), name='descargar_excel_categoria'),
    path('descargar-excel-marca/', admin_required(views.descargar_excel_marca), name='descargar_excel_marca'),
    path('descargar-excel-proveedores/', admin_required(views.descargar_excel_proveedores), name='descargar_excel_proveedores'),
    # Cierre de sesión
    path('logout/', logout_then_login, name='logout'),

]