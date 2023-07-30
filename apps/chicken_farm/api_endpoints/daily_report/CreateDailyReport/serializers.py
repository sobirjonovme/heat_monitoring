from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from apps.chicken_farm.models import DailyReport, FarmResource


class CreateDailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ("laid_eggs", "broken_eggs", "sold_eggs", "dead_chickens")

    def validate(self, data):
        farm_resource = FarmResource.get_solo()

        # check if laid eggs is more than broken eggs
        if data["broken_eggs"] > data["laid_eggs"]:
            raise serializers.ValidationError(
                code="invalid", detail={"broken_eggs": _("Broken eggs can't be more than laid eggs")}
            )

        # check that no chickens died than the available chickens
        if data["dead_chickens"] > farm_resource.chickens_count:
            raise serializers.ValidationError(
                code="invalid", detail={"dead_chickens": _("Dead chickens can't be more than available chickens")}
            )

        # check that no eggs sold than the total available eggs
        if data["sold_eggs"] > farm_resource.eggs_count + data["laid_eggs"]:
            raise serializers.ValidationError(
                code="invalid", detail={"sold_eggs": _("Sold eggs can't be more than total available eggs")}
            )

        return data
