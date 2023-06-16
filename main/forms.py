from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Usuario

from .models import Producto
from .models import Tipo
from .models import Cliente
from .models import Proveedor

class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre','tipo','descripcion',)
        
class TypeForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = ('nombre','descripcion',)

class ClientForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('nombre','apellidoPaterno', 'apellidoMaterno', 'run', 'correo')

class ProviderForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ('nombre','rut', 'correo', 'direccion')

class UserForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'run', 'first_name', 'last_name', 'email', 'password1', 'password2']
