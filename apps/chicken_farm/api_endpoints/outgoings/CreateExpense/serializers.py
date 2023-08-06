from rest_framework import serializers

from apps.chicken_farm.models import FarmExpense
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class CreateFarmExpenseSerializer(serializers.ModelSerializer):
    type = FarmExpenseTypeSerializer()

    class Meta:
        model = FarmExpense
        fields = (
            "type",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "image",
        )
