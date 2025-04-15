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
    list_display = ('cliente', 'auto', 'fecha', 'Empleado', 'MetodoPago')
    list_filter = ('fecha', 'Empleado', 'MetodoPago')
    search_fields = ('cliente__nombre', 'auto__marca', 'Empleado__nombre')
    date_hierarchy = 'fecha'

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puesto', 'email', 'telefono')
    search_fields = ('nombre', 'puesto')

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)


