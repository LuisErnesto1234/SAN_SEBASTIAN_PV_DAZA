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
    path('editar-producto/<int:codigo_producto>',views.editarProducto,name="editarProductoLink"),
    # CRUD DE CATEGORIAS
    path('crear-categoria/',views.crearCategoria,name="crearCategoriaLink"),
    path('editar-categoria/<int:codigo_categoria>',views.editarCategoria,name="editarCategoriaLink"),
    # CRUD DE MARCA
    path('crear-marca/',views.crearMarca,name="crearMarcaLink"),
    path('editar-marca/<int:codigo_marca>',views.editarMarca,name="editarMarcaLink"),
    # CRUD DE PROVEEDOR
    path('crear-proveedor/',views.crearProveedor,name="crearProveedorink"),
    path('editar-proveedor/<int:codigo_proveedor>',views.editarProveedor,name="editarProveedorLink"),
    
    
]

