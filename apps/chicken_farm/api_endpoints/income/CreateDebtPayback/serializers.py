from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.models import FarmIncomeDebtPayback
from apps.common.choices import DebtPaybackMethod


class CreateDebtPaybackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmIncomeDebtPayback
        fields = ("sales_report", "amount", "payment_method")

    def validate(self, data):
        # check if amount is NOT more than sales debt
        if data["amount"] - data["sales_report"].debt_payment > 0:
            raise serializers.ValidationError(code="invalid", detail={"amount": _("Amount is more than sales debt")})

        return data

    def create(self, validated_data):
        # update sales report
        # Reduce debt by amount
        sales_report = validated_data["sales_report"]
        sales_report.debt_payment -= validated_data["amount"]
        # increase the amount of money paid
        if validated_data["payment_method"] == DebtPaybackMethod.CARD:
            sales_report.card_payment += validated_data["amount"]
        elif validated_data["payment_method"] == DebtPaybackMethod.CASH:
            sales_report.cash_payment += validated_data["amount"]
        sales_report.save()

        return super().create(validated_data)
