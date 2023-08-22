from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.choices import FarmDebtPaybackType
from apps.chicken_farm.models import FarmDebtPayback


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
        instance = super().create(validated_data)
        # update expense or sales report according to debt payback
        instance.apply_to_report()

        return instance
