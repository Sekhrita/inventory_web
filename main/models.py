from django.db import models

#Modelo: Tipo de producto
class Tipo(models.Model):
    nombre = models.CharField(max_length = 100)
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre


#Modelo: Producto
class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    tipo = models.ForeignKey(Tipo, on_delete = models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add = True)

    stock = models.PositiveBigIntegerField()

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
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.producto
    

#Modelo: Ingreso
class Ingreso(models.Model):
    producto = models.ForeignKey(Proveedor, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now_add = True)

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