# Generated by Django 4.2.2 on 2023-08-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_farm', '0013_farmdailyreport_via_sales_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmsalesreport',
            name='price_per_box',
            field=models.PositiveIntegerField(verbose_name='price per box'),
        ),
        migrations.AlterField(
            model_name='farmsalesreport',
            name='sold_egg_boxes',
            field=models.PositiveIntegerField(help_text='sold eggs in boxes', verbose_name='sold eggs'),
        ),
    ]
