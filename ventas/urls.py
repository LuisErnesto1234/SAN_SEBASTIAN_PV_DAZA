from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.PageInicio,name="PageInicioLink"),
    path('productos/',views.PageProductos,name="PageProductosLink"),
]
