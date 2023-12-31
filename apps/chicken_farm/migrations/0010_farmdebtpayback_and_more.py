# Generated by Django 4.2.2 on 2023-08-06 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chicken_farm', '0009_alter_farmoutgoingsdebtpayback_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmDebtPayback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('type', models.CharField(choices=[('INCOME', 'Income'), ('OUTGOINGS', 'Outgoings')], max_length=15, verbose_name='Type')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Money amount')),
                ('payment_method', models.CharField(choices=[('CARD', 'Card'), ('CASH', 'Cash')], max_length=15, verbose_name='Payment method')),
                ('paid_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='paid at')),
                ('expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debt_paybacks', to='chicken_farm.farmexpense', verbose_name='expense')),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Reported by')),
                ('sales_report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debt_paybacks', to='chicken_farm.farmsalesreport', verbose_name='Sales report')),
            ],
            options={
                'verbose_name': 'Debt payback',
                'verbose_name_plural': 'Debt paybacks',
            },
        ),
        migrations.RemoveField(
            model_name='farmoutgoingsdebtpayback',
            name='expense',
        ),
        migrations.RemoveField(
            model_name='farmoutgoingsdebtpayback',
            name='reported_by',
        ),
        migrations.DeleteModel(
            name='FarmIncomeDebtPayback',
        ),
        migrations.DeleteModel(
            name='FarmOutgoingsDebtPayback',
        ),
    ]
