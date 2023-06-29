from unicodedata import category
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Tipo)
admin.site.register(Cliente)
admin.site.register(Proveedor)
