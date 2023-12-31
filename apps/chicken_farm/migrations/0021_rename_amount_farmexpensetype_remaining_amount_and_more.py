# Generated by Django 4.2.2 on 2023-09-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_farm', '0020_alter_farmfodderingredientusage_remaining_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmexpensetype',
            old_name='amount',
            new_name='remaining_amount',
        ),
        migrations.RemoveField(
            model_name='farmexpense',
            name='item_unit',
        ),
        migrations.AddField(
            model_name='farmexpensetype',
            name='item_unit',
            field=models.CharField(default='kg', max_length=127, verbose_name='item unit'),
            preserve_default=False,
        ),
    ]
