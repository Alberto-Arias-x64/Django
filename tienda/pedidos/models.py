from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30, verbose_name="Donde vives")
    email=models.EmailField(blank=True , null=True)
    telefono=models.CharField(max_length=7)
    def __str__(self):
        return self.nombre
class articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()
    def __str__(self):
        return 'El nombre es  %s de la seccion  %s y tiene un precio de  %s ' %(self.nombre, self.seccion, self.precio)
class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField(max_length=30)
    entregado=models.BooleanField()