from rest_framework import serializers

from apps.chicken_farm.models import FarmDailyReport, FarmSalesReport
from apps.chicken_farm.utils import bulk_update_daily_reports


class SalesReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmSalesReport
        fields = (
            "id",
            "sold_at",
            "sold_egg_boxes",
            "price_per_box",
            "comment",
            "card_payment",
            "cash_payment",
            "debt_payment",
            "total_payment",
        )

    def create(self, validated_data):
        obj = super().create(validated_data)
        related_daily_report = FarmDailyReport.objects.filter(date=obj.sold_at.date()).first()
        if not related_daily_report:
            related_daily_report = FarmDailyReport.objects.create(date=obj.sold_at.date(), via_sales_report=True)
        bulk_update_daily_reports(related_daily_report)
        return obj
