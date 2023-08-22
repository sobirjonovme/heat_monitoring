from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.models import FarmResource, FarmSalesReport
from apps.chicken_farm.utils import bulk_update_daily_reports


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

        return data

    def create(self, validated_data):
        # get farm resource
        obj = super().create(validated_data)
        obj.debt_payment = obj.total_payment - obj.card_payment - obj.cash_payment
        obj.save()

        from apps.chicken_farm.models import FarmDailyReport

        # get last daily report
        daily_report = FarmDailyReport.objects.filter(date=obj.sold_at.date()).first()
        if daily_report:
            bulk_update_daily_reports(daily_report)

        return obj
