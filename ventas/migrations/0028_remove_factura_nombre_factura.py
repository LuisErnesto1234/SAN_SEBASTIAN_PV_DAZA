# Generated by Django 5.0.3 on 2024-04-24 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0027_alter_productosinunidad_stock_en_kilos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='nombre_factura',
        ),
    ]
