# Generated by Django 4.2.2 on 2023-06-30 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_order_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]
