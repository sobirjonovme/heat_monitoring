from rest_framework import serializers

from apps.chicken_farm.models import FarmDailyReport


class DailyReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmDailyReport
        fields = (
            "laid_eggs",
            "broken_eggs",
            "sold_eggs",
            "dead_chickens",
            "total_remaining_eggs",
            "productivity",
            "date",
        )
