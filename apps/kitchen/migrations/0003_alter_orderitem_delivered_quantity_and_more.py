# Generated by Django 4.2.2 on 2023-07-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_order_delivered_by_order_ordered_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='delivered_quantity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Delivered quantity'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price'),
        ),
    ]
