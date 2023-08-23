# Generated by Django 4.2.2 on 2023-08-23 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_farm', '0015_remove_farmresource_chickens_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmresource',
            name='initial_chickens_count',
            field=models.PositiveIntegerField(default=0, verbose_name='initial chickens count'),
        ),
        migrations.AlterField(
            model_name='farmresource',
            name='initial_eggs_count',
            field=models.PositiveIntegerField(default=0, verbose_name='initial eggs count'),
        ),
    ]