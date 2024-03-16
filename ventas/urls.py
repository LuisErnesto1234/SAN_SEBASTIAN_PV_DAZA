from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.PageInicio,name="PageInicioLink"),
    path('productos/',views.PageProductos,name="PageProductosLink"),
    path('productos-Categorias/',views.PageProductosCategorias,name="PageProductosCategoriasLink"),
    path('productos-Marcas/',views.PageProductosMarcas,name="PageProductosMarcasLink"),
    path('productos-Proveedores/',views.PageProductosProveedores,name="PageProductosProveedoresLink"),
    
    # CRUD DE PRODUCTOS
    path('crear-producto/',views.crearProducto,name="crearProductosLink"),
    # CRUD DE CATEGORIAS
    path('crear-categoria/',views.crearCategoria,name="crearCategoriaLink"),
    # CRUD DE MARCA
    path('crear-marca/',views.crearMarca,name="crearMarcaLink"),
    # CRUD DE PROVEEDOR
    path('crear-proveedor/',views.crearProveedor,name="crearProveedorink"),
    
    
]

