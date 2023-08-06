from rest_framework import serializers

from apps.chicken_farm.models import FarmExpense, FarmExpenseType
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class CreateFarmExpenseSerializer(serializers.ModelSerializer):
    type = FarmExpenseTypeSerializer()

    class Meta:
        model = FarmExpense
        fields = (
            "type",
            "item_amount",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "image",
        )

    def create(self, validated_data):
        expense_type = validated_data.pop("type")
        expense_type_obj = FarmExpenseType.objects.create(**expense_type)
        farm_expense = FarmExpense.objects.create(type=expense_type_obj, **validated_data)
        return farm_expense
