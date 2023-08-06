from rest_framework import serializers

from apps.chicken_farm.models import FarmSalesReport


class SalesReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmSalesReport
        fields = (
            "id",
            "sold_at",
            "sold_eggs",
            "price_per_box",
            "comment",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "total_payment",
            "money_difference",
        )
