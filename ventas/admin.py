from django.contrib import admin
from .models import Categoria, Marca, Proveedor, Producto,Inventario,Factura,MetodoPago,Lista_Productos_Factura,Venta_Productos_Factura ,historial, ProductoSinUnidad, Lista_ProductoSinUnidad_Factura
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(MetodoPago)
admin.site.register(Factura)
admin.site.register(Lista_Productos_Factura)
admin.site.register(Venta_Productos_Factura)
admin.site.register(historial)
admin.site.register(ProductoSinUnidad)
admin.site.register(Lista_ProductoSinUnidad_Factura)


# @admin.register(Producto)
# class MiModeloAdmin(admin.ModelAdmin):
#     # Define campos que deseas mostrar en la lista de modelos
#     fields= '__all__'

    # Agrega filtros para facilitar la búsqueda
    # list_filter = ('campo1', 'campo2', ...)

    # Agrega campos de búsqueda para buscar en el panel de administración
    # search_fields = ['campo1', 'campo2', ...]

    # Define campos para la edición en línea
    # inlines = [MiModeloInline]

    # Define campos de solo lectura en la vista de detalle del modelo
    # readonly_fields = ['campo1', 'campo2', ...]

    # Define campos de fecha en los que se puede usar un selector de fecha
    # date_hierarchy = 'fecha_campo'

    # Define el orden en que se muestran los modelos en el panel de administración
    # ordering = ['campo1', 'campo2', ...]

    # Agrega paginación al panel de administración
    # list_per_page = 20

    # Define campos de autocompletar para claves foráneas
    # raw_id_fields = ['foreign_key_field']

    # Define acciones personalizadas para realizar en lotes
    # actions = [custom_action]

    # Define campos para mostrar en la barra lateral del panel de administración
    # list_display_links = ['campo1', 'campo2', ...]

    # Define campos para agrupar registros en la vista del modelo
    # list_editable = ['campo1', 'campo2', ...]

    # Define campos para mostrar como enlaces en la lista del modelo
    # list_display_links = ['campo1', 'campo2', ...]

    # Agrega campos de solo lectura para la edición en línea
    # readonly_fields = ['campo1', 'campo2', ...]

    # Agrega campos para la edición en línea
    # inlines = [MiModeloInline]
