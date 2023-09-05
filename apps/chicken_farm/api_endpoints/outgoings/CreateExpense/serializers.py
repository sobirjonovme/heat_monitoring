from rest_framework import serializers

from apps.chicken_farm.choices import FarmExpenseCategory
from apps.chicken_farm.models import FarmExpense, FarmExpenseType
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class CreateFarmExpenseSerializer(serializers.ModelSerializer):
    type = FarmExpenseTypeSerializer(read_only=True)
    type_name = serializers.CharField(write_only=True, max_length=255, required=True)
    item_unit = serializers.CharField(write_only=True, max_length=127, required=True)
    expense_category = serializers.ChoiceField(write_only=True, choices=FarmExpenseCategory.choices, required=True)

    class Meta:
        model = FarmExpense
        fields = (
            "item_amount",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "comment",
            "image",
            # # read only fields
            "type",
            # write only fields
            "type_name",
            "item_unit",
            "expense_category",
        )

    def create(self, validated_data):
        # get or create expense type
        type_name = validated_data.pop("type_name")
        expense_category = validated_data.pop("expense_category")
        item_unit = validated_data.pop("item_unit")
        expense_type_obj, _ = FarmExpenseType.objects.get_or_create(
            name=type_name, defaults={"category": expense_category, "item_unit": item_unit}
        )

        # create farm expense
        farm_expense = FarmExpense.objects.create(type=expense_type_obj, **validated_data)

        # increase expense type amount
        farm_expense.increase_expense_type_amount()

        return farm_expense
