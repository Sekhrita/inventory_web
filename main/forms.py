from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Producto
from .models import Tipo

class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre','tipo','descripcion',)
        

class TypeForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = ('nombre','descripcion',)

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
