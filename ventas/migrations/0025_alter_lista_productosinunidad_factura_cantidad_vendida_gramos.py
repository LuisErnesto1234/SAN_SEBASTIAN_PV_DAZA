# Generated by Django 5.0.3 on 2024-04-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0024_alter_lista_productosinunidad_factura_cantidad_vendida_gramos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista_productosinunidad_factura',
            name='cantidad_vendida_gramos',
            field=models.DecimalField(decimal_places=1, max_digits=6),
        ),
    ]