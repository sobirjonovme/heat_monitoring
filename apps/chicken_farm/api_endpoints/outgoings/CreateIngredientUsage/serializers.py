from rest_framework import serializers

from apps.chicken_farm.models import FarmFodderIngredientUsage


class CreateIngredientUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmFodderIngredientUsage
        fields = (
            "ingredient",
            "amount",
        )

    def create(self, validated_data):
        # create farm fodder ingredient usage
        ingredient_usage = FarmFodderIngredientUsage.objects.create(**validated_data)
        # reduce ingredient amount
        ingredient_usage.reduce_ingredient_amount()

        return ingredient_usage
