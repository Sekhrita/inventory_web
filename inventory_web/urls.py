"""
URL configuration for inventory_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from main.views import *

urlpatterns = [
    #Sección: Inicio
    path('', index, name = 'index'),
    path('presentation/', explain_lab, name = 'explain_lab'),
    path('equipment/', show_lab, name = 'show_lab'),


    #Sección: Inventario (producto)
    path('product/', list_product, name = 'list_product'),
    path('add_product/', add_product, name = 'add_product'),
    path('vis_product/<int:pk>/', vis_product, name = 'vis_product'),
    path('edit_product/<int:pk>/', edit_product, name = 'edit_product'),
    path('del_product/<int:pk>/', del_product, name = 'del_product'),

    #Sección: Inventario (categoría)
    path('type/', list_type, name = 'list_type'),
    path('add_type/', add_type, name = 'add_type'),
    path('vis_type/<int:pk>/', vis_type, name = 'vis_type'),
    path('edit_type/<int:pk>/', edit_type, name = 'edit_type'),
    path('del_type/<int:pk>/', del_type, name = 'del_type'),


    #Sección: Movimientos de inventario (seleccionar producto)
    path('management/', management, name = 'management'),

    #Sección: Movimientos de inventario (manejar producto)
    path('entry/<int:pk>/', entry, name = 'entry'),
    path('discharge/<int:pk>/', discharge, name = 'discharge'),

    #Sección: Movimientos de inventario (seleccionar producto en caso de carrito)
    path('cart_management_entry/<int:pk>/', cart_management_entry, name = 'cart_management_entry'),
    path('cart_management_discharge/<int:pk>/', cart_management_discharge, name = 'cart_management_discharge'),

    #Sección: Movimientos de inventario (manejar producto en caso de carrito)
    path('in_product/<int:cart>/<int:pk>/', in_product, name = 'in_product'),
    path('out_product/<int:cart>/<int:pk>/', out_product, name = 'out_product'),

    #Sección: Ver carrito
    path('vis_cart_management_entry/<int:cart>', vis_cart_management_entry, name='vis_cart_management_entry'),
    path('vis_cart_management_discharge/<int:cart>', vis_cart_management_discharge, name='vis_cart_management_discharge'),

    #Sección: Efectuar carrito
    path('confirm_cart_management_entry/<int:cart>', confirm_cart_management_entry, name='confirm_cart_management_entry'),
    path('confirm_cart_management_discharge/<int:cart>', confirm_cart_management_discharge, name='confirm_cart_management_discharge'),

    #Sección: Movimientos de inventario (historial)


    #Sección: Datos (cliente)
    path('client/', list_client, name = 'list_client'),
    path('add_client/', add_client, name = 'add_client'),
    path('edit_client/<int:pk>/', edit_client, name = 'edit_client'),
    path('del_client/<int:pk>/', del_client, name = 'del_client'),

    #Sección: Datos (proveedor)
    path('provider/', list_provider, name = 'list_provider'),
    path('add_provider/', add_provider, name = 'add_provider'),
    path('edit_provider/<int:pk>/', edit_provider, name = 'edit_provider'),
    path('del_provider/<int:pk>/', del_provider, name = 'del_provider'),
    

    #Sección: Administración (admin django)
    path('admin/', admin.site.urls),


    #Sección: Login (usuario)
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro', registro, name = 'registro'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)