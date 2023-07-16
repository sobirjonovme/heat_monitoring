# Generated by Django 4.2.2 on 2023-07-16 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('status', models.CharField(choices=[('new', 'New'), ('delivered', 'Delivered'), ('checked', 'Checked')], default='new', max_length=15, verbose_name='Status')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=127, verbose_name='Name')),
                ('short_name', models.CharField(max_length=15, verbose_name='Short name')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kitchen.productunit', verbose_name='Unit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('needed_quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Unit quantity')),
                ('delivered_quantity', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Delivered quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('is_checked', models.BooleanField(default=False, verbose_name='Is checked')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='kitchen.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='kitchen.product', verbose_name='Product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
