from rest_framework import serializers

from apps.chicken_farm.models import FarmDebtPayback


class FarmDebtPaybackListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmDebtPayback
        fields = (
            "id",
            "sales_report",
            "expense",
            "type",
            "amount",
            "payment_method",
            "paid_at",
        )
