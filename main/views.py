from django.shortcuts import render
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, 'Subido')
        else:
            messages.error('Error al subir')
    
    product_form = ProductForm()
    return render(request, 'main/product_list.html', {'products':products, 'formulario':product_form})
