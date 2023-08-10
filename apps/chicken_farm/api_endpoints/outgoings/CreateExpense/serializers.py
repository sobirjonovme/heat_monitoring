from rest_framework import serializers

from apps.chicken_farm.models import FarmExpense, FarmExpenseType
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class CreateFarmExpenseSerializer(serializers.ModelSerializer):
    type = FarmExpenseTypeSerializer(read_only=True)
    type_name = serializers.CharField(write_only=True, max_length=255, required=True)

    class Meta:
        model = FarmExpense
        fields = (
            "item_amount",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "image",
            # read only fields
            "type",
            # write only fields
            "type_name",
        )

    def create(self, validated_data):
        type_name = validated_data.pop("type_name")
        expense_type_obj = FarmExpenseType.objects.create(name=type_name)
        farm_expense = FarmExpense.objects.create(type=expense_type_obj, **validated_data)
        return farm_expense
