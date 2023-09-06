from rest_framework import serializers

from apps.chicken_farm.models import FarmExpenseType, FarmFodderIngredientUsage


class IngredientShortDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmExpenseType
        fields = (
            "id",
            "name",
            "item_unit",
        )
        ref_name = "FarmFodderUsageIngredientShortDetailSerializer"


class IngredientUsageListSerializer(serializers.ModelSerializer):
    ingredient = IngredientShortDetailSerializer(read_only=True)

    class Meta:
        model = FarmFodderIngredientUsage
        fields = (
            "id",
            "ingredient",
            "amount",
            "date",
        )
        ref_name = "FarmFodderIngredientUsageListSerializer"
