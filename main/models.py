from django.db import models
from django.utils import timezone


#Modelo: Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length = 100)
    apellidoPaterno = models.CharField(max_length = 100)
    apellidoMaterno = models.CharField(max_length = 100)
    run = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 254)

    def __str__(self):
        return f"[{self.run}] {self.nombre} "
    

#Modelo: Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length = 100)
    rut = models.CharField(max_length = 100)
    correo = models.EmailField(max_length = 254)
    direccion = models.CharField(max_length = 100)

    def __str__(self):
        return f"[{self.rut}] {self.nombre}"
    

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
    tipo = models.ForeignKey(Tipo, on_delete = models.RESTRICT)
    descripcion = models.TextField(default="---")

    #información principal: ATRIBUTO VITAL
    stock = models.PositiveBigIntegerField(default=0)

    #información expandida
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_edicion = models.DateTimeField(auto_now=True)
    encargado = models.CharField(max_length = 100, default="Anonimo")

    def __str__(self):
        return self.nombre
    

#Modelo: Egreso
class Ingreso(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete = models.RESTRICT)

    fechaMovimiento = models.DateField(default=timezone.now)
    fechaSistema = models.DateTimeField(auto_now_add = True)
    gestor = models.CharField(max_length = 100, default="Anonimo")

    def __str__(self):
        return self.proveedor

#Modelo: Egreso
class IngresoProducto(models.Model):
    ingreso = models.ForeignKey(Ingreso, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.RESTRICT)

    cantIngreso = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.cantIngreso} x {self.producto.nombre} x {self.ingreso}"



#Modelo: Egreso
class Egreso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.RESTRICT)

    fechaMovimiento = models.DateField(default=timezone.now)
    fechaSistema = models.DateTimeField(auto_now_add = True)
    gestor = models.CharField(max_length = 100, default="Anonimo")

    def __str__(self):
        return self.cliente
    

#Modelo: Egreso
class EgresoProducto(models.Model):
    egreso = models.ForeignKey(Egreso, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.RESTRICT)

    cantEgreso = models.PositiveBigIntegerField()

    def __str__(self):
        return f"{self.cantEgreso} - {self.producto.nombre} - {self.egreso}"