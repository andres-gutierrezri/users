from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " - " + self.user.username


class Factura(models.Model):
    numero_factura = models.IntegerField(null=False, blank=False)
    nombre = models.TextField(max_length=100)
    direccion = models.TextField(max_length=100)
    telefono = models.IntegerField(null=True, blank=True)
    fecha_nacimineto = models.DateTimeField(null=True, blank=True)
    genero = models.TextField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " - " + self.user.username


class Detalle_Factura(models.Model):
    numero_factura = models.IntegerField(null=False, blank=False)
    valor_unitario = models.IntegerField(null=False, blank=False)
    cantidad = models.IntegerField(null=False, blank=False)
    iva = models.IntegerField(null=False, blank=False)
    fecha = models.DateTimeField(null=True, blank=True)
    total = models.IntegerField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_factura + " - " + self.user.username


class Pago(models.Model):
    numero_pago = models.IntegerField(null=False, blank=False)
    forma_de_pago = models.TextField(max_length=100)
    cantidad = models.IntegerField(null=False, blank=False)
    fecha = models.DateTimeField(null=True, blank=True)
    total = models.IntegerField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.numer_pago + " - " + self.user.username


class Carrito(models.Model):
    productos = models.TextField(max_length=100)
    fecha = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.productos + " - " + self.user.username


class Pedido(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=100)
    precio = models.IntegerField(null=False, blank=False)
    categoria = models.TextField(max_length=100)
    fecha = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " - " + self.user.username
