from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.choices import FarmDebtPaybackType
from apps.chicken_farm.models import FarmDebtPayback
from apps.common.choices import DebtPaybackMethod


class CreateDebtPaybackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmDebtPayback
        fields = ("type", "expense", "sales_report", "amount", "payment_method")

    def validate(self, data):
        # if type is income
        if data["type"] == FarmDebtPaybackType.INCOME:
            data["expense"] = None
            # check if amount is NOT more than sales debt
            if data["amount"] - data["sales_report"].debt_payment > 0:
                raise serializers.ValidationError(
                    code="invalid", detail={"amount": _("Amount is more than sales debt")}
                )

        # if type is outgoings
        elif data["type"] == FarmDebtPaybackType.OUTGOINGS:
            data["sales_report"] = None
            # check if amount is NOT more than expense debt
            if data["amount"] - data["expense"].debt_payment > 0:
                raise serializers.ValidationError(
                    code="invalid", detail={"amount": _("Amount is more than expense debt")}
                )

        return data

    def create(self, validated_data):
        # if type is income
        if validated_data["type"] == FarmDebtPaybackType.INCOME:
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

        # if type is outgoings
        elif validated_data["type"] == FarmDebtPaybackType.OUTGOINGS:
            # update expense
            # Reduce debt by amount
            expense = validated_data["expense"]
            expense.debt_payment -= validated_data["amount"]
            # increase the amount of money paid
            if validated_data["payment_method"] == DebtPaybackMethod.CARD:
                expense.card_payment += validated_data["amount"]
            elif validated_data["payment_method"] == DebtPaybackMethod.CASH:
                expense.cash_payment += validated_data["amount"]
            expense.save()

        return super().create(validated_data)
