from django.shortcuts import render
from django.contrib import messages
from .models import Producto
from .forms import ProductForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

# Create your views here.
def product_list(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        productos_form = ProductForm(request.POST)
        if productos_form.is_valid():
            productos_form.save()
            messages.success(request, 'Subido')
        else:
            messages.error('Error al subir')
    
    productos_form = ProductForm()
    return render(request, 'main/product/product_list.html', {'productos':productos, 'formulario':productos_form})
