# Generated by Django 5.0.3 on 2024-04-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0026_alter_productosinunidad_stock_en_kilos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productosinunidad',
            name='stock_en_kilos',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
