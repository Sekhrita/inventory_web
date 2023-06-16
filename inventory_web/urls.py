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
from django.urls import path, include
from main.views import *

urlpatterns = [
    #sección principal de páginas visitables
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),

    #sección de producto
    path('product/', list_product, name = 'list_product'),
    path('add_product/', add_product, name = 'add_product'),
    path('vis_product/<int:pk>/', vis_product, name = 'vis_product'),
    path('edit_product/<int:pk>/', edit_product, name = 'edit_product'),
    path('del_product/<int:pk>/', del_product, name = 'del_product'),

    #sección de categoria
    path('type/', list_type, name = 'list_type'),
    path('add_type/', add_type, name = 'add_type'),
    path('vis_type/<int:pk>/', vis_type, name = 'vis_type'),
    path('edit_type/<int:pk>/', edit_type, name = 'edit_type'),
    path('del_type/<int:pk>/', del_type, name = 'del_type'),

    #sección de gestión de producto

    #sección de usuario
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro', registro, name = 'registro'),

]