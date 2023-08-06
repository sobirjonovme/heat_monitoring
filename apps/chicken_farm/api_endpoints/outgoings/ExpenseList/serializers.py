from rest_framework import serializers

from apps.chicken_farm.models import FarmExpense
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class FarmExpenseListSerializer(serializers.ModelSerializer):
    type = FarmExpenseTypeSerializer()

    class Meta:
        model = FarmExpense
        fields = (
            "id",
            "type",
            "item_amount",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "total_payment",
            "image",
            "date",
        )
