from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Producto
from .models import Tipo
from .forms import ProductForm
from .forms import TypeForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'main/index.html')

# Create your views here.
@login_required
def list_product(request):
    productos = Producto.objects.all()
    return render(request, 'main/product/list_product.html', {'productos':productos})

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
    return render(request, 'main/product/add_product.html', {'formulario':productos_form})

@login_required
def vis_product(request, pk):
    producto = Producto.objects.get(id=pk)

    return render(request, 'main/product/vis_product.html', {'producto':producto})

@login_required
def edit_product(request, pk):
    productos = Producto.objects.get(id=pk)
    if request.method == 'POST':
        productos_form = ProductForm(request.POST, instance=productos)
        if productos_form.is_valid():
            productos_form.save()
            messages.success(request, 'Cambios guardados')
            #return redirect('/product')
        else:
            messages.error('Error al realizar los cambios')
    else:
        productos_form = ProductForm(instance=productos)

    return render(request, 'main/product/edit_product.html', {'formulario':productos_form})

@login_required
def del_product(request, pk):
    productos = Producto.objects.get(id=pk)
    if request.method == 'POST':
        productos.delete()
        return redirect('/product')

    return render(request, 'main/product/del_product.html', {'productos': productos})

@login_required
def list_type(request):
    tipos = Tipo.objects.all()
    return render(request, 'main/type/list_type.html', {'tipos':tipos})

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
    return render(request, 'main/type/add_type.html', {'formulario':tipos_form})

@login_required
def vis_type(request, pk):
    tipo = Tipo.objects.get(id=pk)
    return render(request, 'main/type/vis_type.html', {'tipo':tipo})

@login_required
def edit_type(request, pk):
    tipos = Tipo.objects.get(id=pk)
    if request.method == 'POST':
        tipos_form = TypeForm(request.POST, instance=tipos)
        if tipos_form.is_valid():
            tipos_form.save()
            messages.success(request, 'Cambios guardados')
        else:
            messages.error('Error al realizar los cambios')
    else:
        tipos_form = TypeForm(instance=tipos)

    return render(request, 'main/type/edit_type.html', {'formulario':tipos_form})

@login_required
def del_type(request, pk):
    tipos = Tipo.objects.get(id=pk)
    if request.method == 'POST':
        tipos.delete()
        return redirect('/type')

    return render(request, 'main/type/del_type.html', {'tipos':tipos})