from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.models import FarmDailyReport, FarmResource
from apps.chicken_farm.utils import bulk_update_daily_reports


class CreateDailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmDailyReport
        fields = ("laid_eggs", "broken_eggs", "dead_chickens")

    def validate(self, data):
        farm_resource = FarmResource.get_solo()

        # check if laid eggs is more than broken eggs
        if data["broken_eggs"] > data["laid_eggs"]:
            raise serializers.ValidationError(
                code="invalid", detail={"broken_eggs": _("Broken eggs can't be more than laid eggs")}
            )

        # check that no more chickens died than the available chickens
        if data["dead_chickens"] > farm_resource.current_chickens_count:
            raise serializers.ValidationError(
                code="invalid", detail={"dead_chickens": _("Dead chickens can't be more than available chickens")}
            )

        return data

    def create(self, validated_data):

        obj = super().create(validated_data)

        bulk_update_daily_reports(obj)
        return obj
