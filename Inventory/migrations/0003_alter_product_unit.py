# Generated by Django 5.0.4 on 2024-04-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Gr', 'Grams'), ('Lt', 'Liters'), ('Un', 'Units'), ('Kl', 'Kilograms')], default='KG', max_length=2),
        ),
    ]
