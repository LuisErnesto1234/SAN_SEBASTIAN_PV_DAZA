from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.PageInicio,name="PageInicioLink"),
    # SECCION DE VENTAS
    path('ventas',views.PageVentas,name="PageVentasLink"),
    path('crear-ventas/<int:cod_fac>',views.crearVenta,name="crearVentaLink"),
    path('procesar-ventas/<int:cod_fac>',views.procesarVenta,name="procesarVentaLink"),

    # SECCION DE PRODUCTOS
    path('productos/',views.PageProductos,name="PageProductosLink"),
    path('productos-Categorias/',views.PageProductosCategorias,name="PageProductosCategoriasLink"),
    path('productos-Marcas/',views.PageProductosMarcas,name="PageProductosMarcasLink"),
    path('productos-Proveedores/',views.PageProductosProveedores,name="PageProductosProveedoresLink"),
    
    # CRUD DE PRODUCTOS
    path('crear-producto/',views.crearProducto,name="crearProductosLink"),
    path('editar-producto/<int:codigo_producto>',views.editarProducto,name="editarProductoLink"),
    path('eliminar-producto/<int:codigo_producto>',views.eliminarProducto,name="eliminarProductoLink"),
    path('detalle-producto/<int:codigo_producto>',views.detalleProducto,name="detalleProductoLink"),
    # CRUD DE CATEGORIAS
    path('crear-categoria/',views.crearCategoria,name="crearCategoriaLink"),
    path('editar-categoria/<int:codigo_categoria>',views.editarCategoria,name="editarCategoriaLink"),
    path('eliminar-categoria/<int:codigo_categoria>',views.eliminarCategoria,name="eliminarCategoriaLink"),
    # CRUD DE MARCA
    path('crear-marca/',views.crearMarca,name="crearMarcaLink"),
    path('editar-marca/<int:codigo_marca>',views.editarMarca,name="editarMarcaLink"),
    path('eliminar-marca/<int:codigo_marca>',views.eliminarMarca,name="eliminarMarcaLink"),
    # CRUD DE PROVEEDOR
    path('crear-proveedor/',views.crearProveedor,name="crearProveedorink"),
    path('editar-proveedor/<int:codigo_proveedor>',views.editarProveedor,name="editarProveedorLink"),
    path('eliminar-proveedor/<int:codigo_proveedor>',views.eliminarProveedor,name="eliminarProveedorLink"),
    #Descargar mi csv
    path('descargar-excel/', views.descargar_excel, name='descargar_excel'),
    path('descargar-excel-categoria/', views.descargar_excel_categoria, name='descargar_excel_categoria'),
    path('descargar-excel-marca/', views.descargar_excel_marca, name='descargar_excel_marca'),
    path('descargar-excel-proveedores/', views.descargar_excel_proveedores, name='descargar_excel_proveedores'),



    
]

