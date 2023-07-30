from rest_framework import serializers

from apps.chicken_farm.models import DailyReport


class DailyReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = (
            "laid_eggs",
            "broken_eggs",
            "sold_eggs",
            "dead_chickens",
            "total_remaining_eggs",
            "productivity",
            "date",
        )
