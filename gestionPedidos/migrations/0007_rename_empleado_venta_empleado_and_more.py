# Generated by Django 5.1.7 on 2025-04-15 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0006_rename_empleado_venta_empleado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='Empleado',
            new_name='empleado',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='MetodoPago',
            new_name='metodo_pago',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
