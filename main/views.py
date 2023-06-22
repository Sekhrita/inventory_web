from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Producto
from .models import Tipo
from .models import Cliente
from .models import Proveedor

from .forms import ProductForm
from .forms import TypeForm
from .forms import ClientForm
from .forms import ProviderForm
from .forms import UserForm
from .forms import IngresoForm
from .forms import EgresoForm

from datetime import datetime


# Create your views here.
@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def explain_lab(request):
    return render(request, 'main/explain_lab.html')

@login_required
def show_lab(request):
    return render(request, 'main/show_lab.html')




@login_required
def list_product(request):
    productos = Producto.objects.all()
    
    contexto = {
        'productos':productos
    }   
    return render(request, 'main/product/product/list_product.html', contexto)

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
    return render(request, 'main/product/product/add_product.html', contexto)

@login_required
def vis_product(request, pk):
    producto = Producto.objects.get(id=pk)

    contexto = {
        'producto': producto,
    }    
    return render(request, 'main/product/product/vis_product.html', contexto)

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
    return render(request, 'main/product/product/edit_product.html', contexto)

@login_required
def del_product(request, pk):
    producto = Producto.objects.get(id=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('/product')

    contexto = {
        'producto': producto,
    }
    return render(request, 'main/product/product/del_product.html', contexto)




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




@login_required
def list_client(request):
    clientes = Cliente.objects.all()

    contexto = {
        'clientes': clientes,
    }
    return render(request, 'main/client/list_client.html', contexto)

@login_required
def add_client(request):
    if request.method == 'POST':
        clientes_form = ClientForm(request.POST)
        if clientes_form.is_valid():
            temp = clientes_form.save(commit=False)
            temp.encargado = request.user
            temp.save()
            messages.success(request, 'Cliente agregado con éxito.')
        else:
            messages.error('Error al subir')

    clientes_form = ClientForm()
    contexto = {
        'formulario': clientes_form,
    }
    return render(request, 'main/client/add_client.html', contexto)

@login_required
def edit_client(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        clientes_form = ClientForm(request.POST, instance=cliente)
        if clientes_form.is_valid():
            temp = clientes_form.save(commit=False)
            fecha_actual = datetime.now()
            temp.fecha_edicion = fecha_actual
            temp.save()
            messages.success(request, 'Cambios guardados')
        else:
            messages.error('Error al realizar los cambios')
    else:
        clientes_form = ClientForm(instance=cliente)

    contexto = {
        'formulario':clientes_form,
        'cliente': cliente,
    }
    return render(request, 'main/client/edit_client.html', contexto)

@login_required
def del_client(request, pk):
    cliente = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/client')

    contexto = {
        'cliente': cliente,
    }
    return render(request, 'main/client/del_client.html', contexto)




@login_required
def list_provider(request):
    proveedores = Proveedor.objects.all()
    
    contexto = {
        'proveedores':proveedores
    }   
    return render(request, 'main/provider/list_provider.html', contexto)

@login_required
def add_provider(request):
    if request.method == 'POST':
        proveedores_form = ProviderForm(request.POST)
        if proveedores_form.is_valid():
            temp = proveedores_form.save(commit=False)
            temp.encargado = request.user
            temp.save()
            messages.success(request, 'Proveedor agregado con éxito.')
        else:
            messages.error('Error al subir')

    proveedores_form = ProviderForm()
    contexto = {
        'formulario':proveedores_form ,
    }   
    return render(request, 'main/provider/add_provider.html', contexto)

@login_required
def edit_provider(request, pk):
    proveedor = Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        proveedores_form = ProviderForm(request.POST, instance=proveedor)
        if proveedores_form .is_valid():
            temp = proveedores_form.save(commit=False)
            fecha_actual = datetime.now()
            temp.fecha_edicion = fecha_actual
            temp.save()
            messages.success(request, 'Cambios guardados')
        else:
            messages.error('Error al realizar los cambios')
    else:
        proveedores_form  = ProviderForm(instance=proveedor)

    contexto = {
        'formulario':proveedores_form ,
        'proveedor': proveedor,
    }
    return render(request, 'main/provider/edit_provider.html', contexto)

@login_required
def del_provider(request, pk):
    proveedor = Proveedor.objects.get(id=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('/provider')

    contexto = {
        'proveedor': proveedor,
    }
    return render(request, 'main/provider/del_provider.html', contexto)




def registro(request):
    if request.method == 'POST':
        usuario_form = UserForm(request.POST)
        if usuario_form.is_valid():
            usuario_form.save()

            user = authenticate(username=usuario_form.cleaned_data['username'],
                                 password=usuario_form.cleaned_data['password1'])

            
            login(request, user)
            return redirect('index')
    else:
        usuario_form = UserForm()

    contexto = {
        'formulario': usuario_form
    }
    return render(request, 'registration/registro.html', contexto)



@login_required
def management(request):
    productos = Producto.objects.all()
    
    contexto = {
        'productos':productos
    }   
    return render(request, 'main/product/product_gestion/management.html', contexto)

@login_required
def in_product(request):
    return render(request, 'main/product/product_gestion/in_product/in_product.html')

@login_required
def out_product(request):  
    return render(request, 'main/product/product_gestion/out_product/out_product.html')

@login_required
def entry(request, pk):  
    producto = Producto.objects.get(id=pk)

    if request.method == 'POST':
        ingreso_form = IngresoForm(request.POST)
        if ingreso_form.is_valid():
            temp = ingreso_form.save(commit=False)
            temp.producto = producto
            temp.gestor = request.user
            temp.save()
            messages.success(request, 'Producto agregado con éxito.')
        else:
            messages.error('Error al subir')    

    ingreso_form = IngresoForm()
    contexto = {
        'formulario': ingreso_form,
        'producto': producto,
    }    
    return render(request, 'main/product/product_gestion/in_product/entry.html', contexto)

@login_required
def discharge(request, pk):  
    producto = Producto.objects.get(id=pk)

    if request.method == 'POST':
        egreso_form = EgresoForm(request.POST)
        if egreso_form.is_valid():
            temp = egreso_form.save(commit=False)
            temp.producto = producto
            temp.gestor = request.user
            temp.save()
            messages.success(request, 'Producto agregado con éxito.')
        else:
            messages.error('Error al subir')    

    egreso_form = EgresoForm()
    contexto = {
        'formulario': egreso_form,
        'producto': producto,
    }    
    return render(request, 'main/product/product_gestion/out_product/discharge.html', contexto)

@login_required
def list_management(request):
    return render(request, 'main/product/product_gestion/list_management.html')

@login_required
def vis_management(request):
    return render(request, 'main/product/product_gestion/vis_management.html')

