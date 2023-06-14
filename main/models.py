from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

#Modelo: Tipo de producto
class Tipo(models.Model):
    #información principal
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(default="---")
    
    #información expandida
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    encargado = models.CharField(max_length = 100, default="Anonimo")

    def __str__(self):
        return self.nombre


#Modelo: Producto
class Producto(models.Model):
    #información principal
    nombre = models.CharField(max_length = 100)
    tipo = models.ForeignKey(Tipo, on_delete = models.CASCADE)
    descripcion = models.TextField(default="---")

    #información principal: ATRIBUTO VITAL
    stock = models.PositiveBigIntegerField(default=0)

    #información expandida
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    encargado = models.CharField(max_length = 100, default="Anonimo")

    def __str__(self):
        return self.nombre




#Modelo: Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidoPaterno = models.CharField(max_length = 100)
    apellidoMaterno = models.CharField(max_length = 100)
    run = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 254)

    def __str__(self):
        return self.run
    

#Modelo: Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length = 100)
    rut = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 254)
    direccion = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre
    



#Modelo: Egreso
class Egreso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    fechaMovimiento = models.DateField(default=timezone.now)
    fechaSistema = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.producto
    

#Modelo: Ingreso
class Ingreso(models.Model):
    producto = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    fechaMovimiento = models.DateField(default=timezone.now)
    fechaSistema = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.producto
    



#Modelo: Egreso
class EgresoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    egreso = models.ForeignKey(Egreso, on_delete = models.CASCADE)

    cantEgreso = models.PositiveBigIntegerField()

    def __str__(self):
        return self.producto
    

#Modelo: Ingreso
class IngresoProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    ingreso = models.ForeignKey(Ingreso, on_delete = models.CASCADE)

    cantIngreso = models.PositiveBigIntegerField()

    def __str__(self):
        return self.producto