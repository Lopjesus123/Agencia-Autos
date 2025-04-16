from django.contrib import admin

from gestionPedidos.models import Clientes,Auto,Venta,Empleado,MetodoPago

# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')
    list_per_page = 20

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'precio', 'disponible')
    list_filter = ('disponible', 'marca', 'año')
    search_fields = ('marca', 'modelo')
    list_per_page = 20

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'auto_detalle', 'fecha', 'empleado_nombre', 'metodo_pago')

    def cliente_nombre(self, obj):
        return obj.cliente.nombre

    def auto_detalle(self, obj):
        return f"{obj.auto.marca} {obj.auto.modelo} {obj.auto.año}"

    def empleado_nombre(self, obj):
        return obj.empleado.nombre if obj.empleado else "Sin asignar"

    def metodo_pago(self, obj):
        return obj.metodo_pago.tipo if obj.metodo_pago else "Sin método"

    list_filter = ('fecha', 'empleado', 'metodo_pago')
    search_fields = ('cliente__nombre', 'auto__marca', 'auto__modelo')



@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puesto', 'email', 'telefono')
    search_fields = ('nombre', 'puesto')

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
