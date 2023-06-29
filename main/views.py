from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Producto
from .models import Tipo
from .models import Cliente
from .models import Proveedor
from .models import Ingreso
from .models import IngresoProducto
from .models import Egreso
from .models import EgresoProducto

from .forms import ProductForm
from .forms import TypeForm
from .forms import ClientForm
from .forms import ProviderForm
from .forms import UserForm
from .forms import IngresoForm
from .forms import IngresoProductoForm
from .forms import EgresoForm
from .forms import EgresoProductoForm


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
def entry(request,pk):
    producto = Producto.objects.get(id=pk)

    if request.method == 'POST':
        ingreso_form = IngresoForm(request.POST)
        ingresoproducto_form = IngresoProductoForm(request.POST)

        if 'ingreso_directo' in request.POST or 'crear_carrito_ingreso' in request.POST:
            if ingreso_form.is_valid() and ingresoproducto_form.is_valid():
                temp_1 = ingreso_form.save(commit=False)
                temp_1.gestor = request.user

                temp_2 = ingresoproducto_form.save(commit=False)
                temp_2.producto = producto
                temp_2.ingreso = temp_1
                
                producto.stock = producto.stock + temp_2.cantIngreso

                temp_1.save()
                temp_2.save()

                if 'crear_carrito_ingreso' in request.POST:
                    url = reverse('cart_management_entry', args=[temp_1.id])
                    return redirect(url)
                    
                elif 'ingreso_directo' in request.POST:
                    producto.save()
                    messages.success(request, 'Stock agregado con éxito.')
                    return redirect('management')

            else:
                messages.error(request, 'Error al realizar el ingreso') 

        elif 'crear_carrito_ingreso' in request.POST:
            if ingreso_form.is_valid():
                temp = ingreso_form.save(commit=False)
                temp.gestor = request.user
                temp.save()

                url = reverse('cart_management_entry', args=[temp.id])
                return redirect(url)
            else:
                messages.error(request, 'Error al crear el carrito')

    ingreso_form = IngresoForm()
    ingresoproducto_form = IngresoProductoForm()
    contexto = {
        'formulario_1': IngresoForm,
        'formulario_2': IngresoProductoForm,
    }
    return render(request, 'main/product/product_gestion/in_product/entry.html', contexto)    

@login_required
def cart_management_entry(request,pk):
    ingreso = Ingreso.objects.get(id=pk)
    
    if request.method == 'POST':
        if 'efectuar_carrito_ingreso' in request.POST:

            return confirm_cart_management_entry(request,pk)

        elif 'ver_carrito_ingreso' in request.POST:
        
            url = reverse('vis_cart_management_entry', args=[pk])
            return redirect(url)
        
        elif 'eliminar_carrito_ingreso' in request.POST:
            ingreso.delete()

            return redirect('management')
        

    productos = Producto.objects.all()
    
    contexto = {
        'productos':productos,
        'ingreso':ingreso,
    }     
    return render(request, 'main/product/product_gestion/cart/cart_management_entry.html', contexto)

@login_required
def in_product(request,cart,pk):
    ingreso = Ingreso.objects.get(id=cart)
    producto = Producto.objects.get(id=pk)

    ingresos_productos = IngresoProducto.objects.all()

    if request.method == 'POST':
        ingresoproducto_form = IngresoProductoForm(request.POST)

        if ingresoproducto_form.is_valid():
            temp = ingresoproducto_form.save(commit=False)
            temp.producto = producto
            temp.ingreso = ingreso

            for iter in ingresos_productos:
                if iter.producto.id == producto.id and iter.ingreso.id == ingreso.id:
                    iter.cantIngreso = temp.cantIngreso + iter.cantIngreso
                    iter.save()

                    messages.success(request, 'Incorporación a un ingreso anterior con exito') 
                    url = reverse('cart_management_entry', args=[cart])
                    return redirect(url)
                    
            temp.save()

            messages.success(request, 'Ingreso añadido al carrito con exito') 

            url = reverse('cart_management_entry', args=[cart])
            return redirect(url)
        
        else:
            messages.error(request, 'Error al añadir el ingreso al carrito') 

    ingresoproducto_form = IngresoProductoForm()
    contexto = {
        'formulario': IngresoProductoForm,
        'ingreso': ingreso,
    }    
    return render(request, 'main/product/product_gestion/in_product/in_product.html', contexto)   

@login_required
def discharge(request,pk):
    producto = Producto.objects.get(id=pk)

    if request.method == 'POST':
        egreso_form = EgresoForm(request.POST)
        egresoproducto_form = EgresoProductoForm(request.POST)

        if 'egreso_directo' in request.POST or 'crear_carrito_egreso' in request.POST:
            if egreso_form.is_valid() and egresoproducto_form.is_valid():
                temp_1 = egreso_form.save(commit=False)
                temp_1.gestor = request.user

                temp_2 = egresoproducto_form.save(commit=False)
                temp_2.producto = producto
                temp_2.egreso = temp_1
                
                if producto.stock >= temp_2.cantEgreso:
                    producto.stock = producto.stock - temp_2.cantEgreso
                        
                    temp_1.save()
                    temp_2.save()

                    if 'crear_carrito_egreso' in request.POST:
                        url = reverse('cart_management_discharge', args=[temp_1.id])
                        return redirect(url)
                        
                    elif 'egreso_directo' in request.POST:
                        producto.save()
                        messages.success(request, 'Stock descargado con éxito.')
                        return redirect('management')

                else:
                    messages.error(request, 'Sin stock suficiente del producto para el egreso') 

            else:
                messages.error(request, 'Error al realizar el egreso') 

        elif 'crear_carrito_egreso' in request.POST:
            if egreso_form.is_valid():
                temp = egreso_form.save(commit=False)
                temp.gestor = request.user
                temp.save()

                url = reverse('cart_management_discharge', args=[temp.id])
                return redirect(url)
            else:
                messages.error(request, 'Error al crear el carrito')

    egreso_form = EgresoForm()
    egresoproducto_form = EgresoProductoForm()
    contexto = {
        'formulario_1': EgresoForm,
        'formulario_2': EgresoProductoForm,
    }
    return render(request, 'main/product/product_gestion/out_product/discharge.html', contexto)    

@login_required
def cart_management_discharge(request,pk):
    egreso = Egreso.objects.get(id=pk)
    
    if request.method == 'POST':

        if 'efectuar_carrito_egreso' in request.POST:
            return confirm_cart_management_discharge(request,pk)

        elif 'ver_carrito_egreso' in request.POST:
        
            url = reverse('vis_cart_management_discharge', args=[pk])
            return redirect(url)
        
        elif 'eliminar_carrito_egreso' in request.POST:
            egreso.delete()

            return redirect('management')
        
        
    productos = Producto.objects.all()
    
    contexto = {
        'productos':productos,
        'egreso':egreso,
    }   
    return render(request, 'main/product/product_gestion/cart/cart_management_discharge.html', contexto)

@login_required
def out_product(request,cart,pk):
    egreso = Egreso.objects.get(id=cart)
    producto = Producto.objects.get(id=pk)

    egresos_productos = EgresoProducto.objects.all()

    comprobar = 0
    if request.method == 'POST':
        egresoproducto_form = EgresoProductoForm(request.POST)

        if egresoproducto_form.is_valid():
            temp = egresoproducto_form.save(commit=False)
            temp.producto = producto
            temp.egreso = egreso

            for iter in egresos_productos:
                if iter.producto.id == producto.id and iter.egreso.id == egreso.id:
                    iter.cantEgreso = temp.cantEgreso + iter.cantEgreso

                    if producto.stock >= iter.cantEgreso:
                        producto.stock = producto.stock - iter.cantEgreso
                        iter.save()

                        messages.success(request, 'Incorporación a un engreso anterior con exito') 
                        url = reverse('cart_management_discharge', args=[cart])
                        return redirect(url)
                    
                    else:
                        comprobar = 1

            if producto.stock >= temp.cantEgreso and comprobar == 0:
                producto.stock = producto.stock - temp.cantEgreso
                        
                temp.save()

                messages.success(request, 'Egreso añadido al carrito con exito') 
                url = reverse('cart_management_discharge', args=[cart])
                return redirect(url)
            else:
                messages.error(request, 'Sin stock suficiente para ese egreso')  

    egresoproducto_form = EgresoProductoForm()
    contexto = {
        'formulario': EgresoProductoForm,
        'egreso': egreso,
    }    
    return render(request, 'main/product/product_gestion/out_product/out_product.html', contexto)   


@login_required
def vis_cart_management_entry(request,cart):
    ingreso = Ingreso.objects.get(id=cart)
    productos = Producto.objects.all()
    ingresosproductos = IngresoProducto.objects.all()

    if request.method == 'POST':
        if 'efectuar_carrito_ingreso' in request.POST:

            return confirm_cart_management_entry(request,cart)
    
    contexto = {
        'ingreso': ingreso,
        'productos': productos,
        'ingresosproductos': ingresosproductos,
    }
    return render(request, 'main/product/product_gestion/cart/vis_cart_management_entry.html', contexto)

@login_required
def vis_cart_management_discharge(request,cart):
    egreso = Egreso.objects.get(id=cart)
    productos = Producto.objects.all()
    egresosproductos = EgresoProducto.objects.all()

    if request.method == 'POST':
        if 'efectuar_carrito_egreso' in request.POST:
            return confirm_cart_management_discharge(request,cart)
    
    contexto = {
        'egreso': egreso,
        'productos': productos,
        'egresosproductos': egresosproductos,
    }
    return render(request, 'main/product/product_gestion/cart/vis_cart_management_discharge.html', contexto)


@login_required
def confirm_cart_management_entry(request,cart):
    ingreso = Ingreso.objects.get(id=cart)
    productos = Producto.objects.all()
    ingresosproductos = IngresoProducto.objects.all()

    for ingresoproducto in ingresosproductos:
        for producto in productos:
            if ingresoproducto.ingreso.id == ingreso.id and ingresoproducto.producto.id == producto.id:
                producto.stock = producto.stock + ingresoproducto.cantIngreso
                producto.save()


    return redirect('management')

@login_required
def confirm_cart_management_discharge(request,cart):
    egreso = Egreso.objects.get(id=cart)
    productos = Producto.objects.all()
    egresosproductos = EgresoProducto.objects.all()

    for egresoproducto in egresosproductos:
        for producto in productos:
            if egresoproducto.egreso.id == egreso.id and egresoproducto.producto.id == producto.id:
                producto.stock = producto.stock - egresoproducto.cantEgreso
                producto.save()


    return redirect('management')


@login_required
def list_management(request):
    ingresos = Ingreso.objects.all()
    egresos = Egreso.objects.all()

    productos = Producto.objects.all()
    
    contexto = {
        'ingresos': ingresos,
        'egresos': egresos,
        'productos': productos,
    }
    return render(request, 'main/product/product_gestion/list_management.html', contexto)


@login_required
def vis_management_entry(request,cart):
    ingreso = Ingreso.objects.get(id=cart)

    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    ingresosproductos = IngresoProducto.objects.all()
    
    contexto = {
        'ingreso': ingreso,
        'proveedores': proveedores,
        'productos': productos,
        'ingresosproductos': ingresosproductos,
    }
    return render(request, 'main/product/product_gestion/vis_management_entry.html', contexto)

@login_required
def vis_management_discharge(request,cart):
    egreso = Egreso.objects.get(id=cart)

    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    egresosproductos = EgresoProducto.objects.all()
    
    contexto = {
        'egreso': egreso,
        'proveedores': proveedores,
        'productos': productos,
        'egresosproductos': egresosproductos,
    }
    return render(request, 'main/product/product_gestion/vis_management_discharge.html', contexto)
