from rest_framework import serializers

from apps.chicken_farm.models import FarmIncomeDebtPayback


class DebtPaybackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmIncomeDebtPayback
        fields = (
            "id",
            "sales_report",
            "amount",
            "payment_method",
            "paid_at",
        )
