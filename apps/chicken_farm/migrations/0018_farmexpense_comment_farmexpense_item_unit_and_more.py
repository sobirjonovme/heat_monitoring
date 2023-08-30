# Generated by Django 4.2.2 on 2023-08-30 17:00

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chicken_farm', '0017_farmsalesreport_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmexpense',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='comment'),
        ),
        migrations.AddField(
            model_name='farmexpense',
            name='item_unit',
            field=models.CharField(default='kg', max_length=127, verbose_name='item unit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmexpensetype',
            name='category',
            field=models.CharField(choices=[('FODDER', 'Fodder'), ('OTHER', 'Other')], default='FODDER', max_length=15, verbose_name='category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='farmexpense',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='expenses/%Y/%m/%d/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='farmexpense',
            name='item_amount',
            field=models.FloatField(verbose_name='item amount'),
        ),
    ]