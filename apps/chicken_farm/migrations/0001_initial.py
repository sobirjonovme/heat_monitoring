# Generated by Django 4.2.2 on 2023-07-30 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('laid_eggs', models.PositiveIntegerField(default=0, verbose_name='laid eggs')),
                ('broken_eggs', models.PositiveIntegerField(default=0, verbose_name='broken eggs')),
                ('sold_eggs', models.PositiveIntegerField(default=0, verbose_name='sold eggs')),
                ('dead_chickens', models.PositiveIntegerField(default=0, verbose_name='dead chickens')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
            ],
            options={
                'verbose_name': 'daily report',
                'verbose_name_plural': 'daily reports',
            },
        ),
        migrations.CreateModel(
            name='FarmResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('chickens_count', models.PositiveIntegerField(default=0, verbose_name='chickens count')),
                ('eggs_count', models.PositiveIntegerField(default=0, verbose_name='eggs count')),
            ],
            options={
                'verbose_name': 'farm resource',
                'verbose_name_plural': 'farm resource',
            },
        ),
    ]