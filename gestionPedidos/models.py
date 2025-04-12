from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=10)

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.IntegerField()
    precio = models.IntegerField()
    disponible = models.BooleanField(default=True)  # <- esto es clave

class Venta(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fecha = models.DateField()
    Empleado = models.ForeignKey("Empleado", on_delete=models.SET_NULL, null=True) #Lo traduces así: “Esta venta fue realizada por X empleado.”
    MetodoPago = models.ForeignKey("MetodoPago", on_delete=models.SET_NULL, null=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=30)
    email = models.CharField()
    telefono= models.CharField(max_length=15)

class MetodoPago(models.Model):
    tipo = models.CharField(max_length=30) #Efectivo,Trasferencia,Tarjeta


