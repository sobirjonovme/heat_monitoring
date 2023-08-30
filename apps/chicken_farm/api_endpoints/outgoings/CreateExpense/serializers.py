from rest_framework import serializers

from apps.chicken_farm.choices import FarmExpenseCategory
from apps.chicken_farm.models import FarmExpense, FarmExpenseType
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class CreateFarmExpenseSerializer(serializers.ModelSerializer):
    type = FarmExpenseTypeSerializer(read_only=True)
    type_name = serializers.CharField(write_only=True, max_length=255, required=True)
    expense_category = serializers.ChoiceField(write_only=True, choices=FarmExpenseCategory.choices, required=True)

    class Meta:
        model = FarmExpense
        fields = (
            "item_amount",
            "item_unit",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "comment",
            "image",
            # # read only fields
            "type",
            # write only fields
            "type_name",
            "expense_category",
        )

    def create(self, validated_data):
        type_name = validated_data.pop("type_name")
        expense_category = validated_data.pop("expense_category")
        expense_type_obj, _ = FarmExpenseType.objects.get_or_create(
            name=type_name, defaults={"category": expense_category}
        )
        farm_expense = FarmExpense.objects.create(type=expense_type_obj, **validated_data)
        return farm_expense
