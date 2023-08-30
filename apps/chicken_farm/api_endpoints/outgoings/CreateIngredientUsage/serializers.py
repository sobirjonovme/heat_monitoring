from rest_framework import serializers

from apps.chicken_farm.models import FarmFodderIngredientUsage


class CreateIngredientUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmFodderIngredientUsage
        fields = (
            "ingredient",
            "amount",
        )
