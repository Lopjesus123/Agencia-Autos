# Generated by Django 5.1.7 on 2025-04-11 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_delete_articulos_auto_disponible'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pedidos',
        ),
    ]
