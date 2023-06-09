from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Producto
from .forms import ProductForm


# Create your views here.
@login_required
def index(request):
    return render(request, 'main/index.html')

# Create your views here.
@login_required
def product_list(request):
    productos = Producto.objects.all()
    return render(request, 'main/product/product_list.html', {'productos':productos})

@login_required
def add_product(request):
    if request.method == 'POST':
        productos_form = ProductForm(request.POST)
        if productos_form.is_valid():
            productos_form.save()
            messages.success(request, 'Subido')
        else:
            messages.error('Error al subir')

    productos_form = ProductForm()
    return render(request, 'main/product/add_product.html', {'formulario':productos_form})

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

