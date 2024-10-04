from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("TCliente/",views.clientes,name="cliente"),
    path("TProductos/",views.productos,name="productos"),
    path("TProveedores/",views.proveedores,name="proveedores"),
    path("TInventario/",views.inventario,name="inventario")
]