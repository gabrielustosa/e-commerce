# Generated by Django 4.0.3 on 2022-04-29 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created',)},
        ),
    ]
