# Generated by Django 4.2.2 on 2023-08-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_farm', '0016_alter_farmresource_initial_chickens_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmsalesreport',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone number'),
        ),
    ]
