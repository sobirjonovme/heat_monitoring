from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.models import FarmResource, FarmSalesReport


class CreateSalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmSalesReport
        fields = (
            "sold_egg_boxes",
            "price_per_box",
            "comment",
            "card_payment",
            "cash_payment",
            "debt_payment",
        )

        extra_kwargs = {
            "debt_payment": {"read_only": True},
        }

    def validate(self, data):
        farm_resource = FarmResource.get_solo()
        print(data)

        # Check if there is enough eggs to sell
        if farm_resource.eggs_count < data["sold_egg_boxes"] * 30:
            raise serializers.ValidationError(code="not_enough_eggs", detail=_("There is not enough eggs to sell"))

        # Check if total money is equal to the sum of card, cash and debt money
        # TODO

        return data
