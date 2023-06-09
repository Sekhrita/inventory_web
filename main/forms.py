from django import forms
from .models import Producto
from .models import Tipo

class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre','tipo','descripcion')

class TypeForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = ('nombre',)
