# Generated by Django 4.2.2 on 2023-07-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_farm', '0002_dailyreport_reported_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreport',
            name='total_remaining_eggs',
            field=models.PositiveIntegerField(default=0, verbose_name='total remaining eggs'),
        ),
    ]
