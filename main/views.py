from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Producto
from .models import Tipo
from .forms import ProductForm
from .forms import TypeForm
from datetime import datetime


# Create your views here.
@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def list_product(request):
    productos = Producto.objects.all()
    
    contexto = {
        'productos':productos
    }   
    return render(request, 'main/product/list_product.html', contexto)

@login_required
def add_product(request):
    if request.method == 'POST':
        productos_form = ProductForm(request.POST)
        if productos_form.is_valid():
            temp = productos_form.save(commit=False)
            temp.encargado = request.user
            temp.save()
            messages.success(request, 'Producto agregado con éxito.')
        else:
            messages.error('Error al subir')

    productos_form = ProductForm()
    contexto = {
        'formulario':productos_form,
    }   
    return render(request, 'main/product/add_product.html', contexto)

@login_required
def vis_product(request, pk):
    producto = Producto.objects.get(id=pk)

    contexto = {
        'producto': producto,
    }    
    return render(request, 'main/product/vis_product.html', contexto)

@login_required
def edit_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        productos_form = ProductForm(request.POST, instance=producto)
        if productos_form.is_valid():
            temp = productos_form.save(commit=False)
            fecha_actual = datetime.now()
            temp.fecha_edicion = fecha_actual
            temp.save()
            messages.success(request, 'Cambios guardados')
        else:
            messages.error('Error al realizar los cambios')
    else:
        productos_form = ProductForm(instance=producto)

    contexto = {
        'formulario':productos_form,
        'producto': producto,
    }
    return render(request, 'main/product/edit_product.html', contexto)

@login_required
def del_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('/product')

    contexto = {
        'producto': producto,
    }
    return render(request, 'main/product/del_product.html', contexto)



@login_required
def list_type(request):
    tipos = Tipo.objects.all()

    contexto = {
        'tipos': tipos,
    }
    return render(request, 'main/type/list_type.html', contexto)

@login_required
def add_type(request):
    if request.method == 'POST':
        tipos_form = TypeForm(request.POST)
        if tipos_form.is_valid():
            temp = tipos_form.save(commit=False)
            temp.encargado = request.user
            temp.save()
            messages.success(request, 'Categoría agregado con éxito.')
        else:
            messages.error('Error al subir')

    tipos_form = TypeForm()
    contexto = {
        'formulario': tipos_form,
    }
    return render(request, 'main/type/add_type.html', contexto)

@login_required
def vis_type(request, pk):
    tipo = Tipo.objects.get(id=pk)

    contexto = {
        'tipo': tipo,
    }
    return render(request, 'main/type/vis_type.html', contexto)

@login_required
def edit_type(request, pk):
    tipo = Tipo.objects.get(id=pk)
    if request.method == 'POST':
        tipos_form = TypeForm(request.POST, instance=tipo)
        if tipos_form.is_valid():
            temp = tipos_form.save(commit=False)
            fecha_actual = datetime.now()
            temp.fecha_edicion = fecha_actual
            temp.save()
            messages.success(request, 'Cambios guardados')
        else:
            messages.error('Error al realizar los cambios')
    else:
        tipos_form = TypeForm(instance=tipo)

    contexto = {
        'formulario':tipos_form,
        'tipo': tipo,
    }
    return render(request, 'main/type/edit_type.html', contexto)

@login_required
def del_type(request, pk):
    tipo = Tipo.objects.get(id=pk)
    if request.method == 'POST':
        tipo.delete()
        return redirect('/type')

    contexto = {
        'tipo': tipo,
    }
    return render(request, 'main/type/del_type.html', contexto)