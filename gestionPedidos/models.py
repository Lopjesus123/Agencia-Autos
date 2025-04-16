from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nombre} ({self.email})"


class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    año = models.IntegerField()
    precio = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"


class MetodoPago(models.Model):
    tipo = models.CharField(max_length=30)  # Efectivo, Transferencia, Tarjeta

    def __str__(self):
        return self.tipo


class Venta(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    fecha = models.DateField()
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.fecha} - {self.cliente.nombre} compró {self.auto.marca} {self.auto.modelo} ({self.auto.año}) por medio de {self.empleado.nombre}"



