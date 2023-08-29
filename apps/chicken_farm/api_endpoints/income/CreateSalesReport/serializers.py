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
            "phone_number",
        )

        extra_kwargs = {
            "debt_payment": {"read_only": True},
        }

    def validate(self, data):
        farm_resource = FarmResource.get_solo()
        print(data)

        # Check if there is enough eggs to sell
        if farm_resource.current_eggs_count < data["sold_egg_boxes"] * 30:
            raise serializers.ValidationError(code="not_enough_eggs", detail=_("There is not enough eggs to sell"))

        # Check if money amount is valid
        if data["sold_egg_boxes"] * data["price_per_box"] < data["card_payment"] + data["cash_payment"]:
            raise serializers.ValidationError(code="invalid_money_amount", detail=_("Invalid money amount"))

        return data

    def create(self, validated_data):
        # get farm resource
        obj = super().create(validated_data)
        obj.debt_payment = obj.total_payment - obj.card_payment - obj.cash_payment
        obj.save()

        # update related daily report
        obj.apply_to_related_daily_report()

        return obj
