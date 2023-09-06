from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.models import FarmFodderIngredientUsage


class CreateIngredientUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmFodderIngredientUsage
        fields = (
            "ingredient",
            "amount",
        )

    def validate(self, data):
        # check ingredient amount
        ingredient = data["ingredient"]
        amount = data["amount"]
        if ingredient.remaining_amount < amount:
            raise serializers.ValidationError(
                code="invalid",
                detail={
                    "amount": _(
                        "There is no such amount of this ingredient." "You can use at most %(amount)s %(unit)s."
                    )
                    % {
                        "amount": ingredient.remaining_amount,
                        "unit": ingredient.item_unit,
                    }
                },
            )

        return data

    def create(self, validated_data):
        # create farm fodder ingredient usage
        ingredient_usage = FarmFodderIngredientUsage.objects.create(**validated_data)
        # reduce ingredient amount
        ingredient_usage.reduce_ingredient_amount()

        return ingredient_usage
