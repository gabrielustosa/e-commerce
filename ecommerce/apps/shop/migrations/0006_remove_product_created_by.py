# Generated by Django 4.0.3 on 2022-04-29 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_in_stock_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
    ]