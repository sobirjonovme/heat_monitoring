from django.db import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chicken_farm.filters import DailyReportFilter, SalesReportFilter
from apps.chicken_farm.models import (FarmDailyReport, FarmResource,
                                      FarmSalesReport)
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin


class IncomeStatisticsAPIView(APIView):
    permission_classes = (IsFarmCounterOrAdmin,)

    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = DailyReportFilter

    def get(self, request, *args, **kwargs):
        daily_reports = DailyReportFilter(request.GET, queryset=FarmDailyReport.objects.all()).qs

        statistics = daily_reports.aggregate(
            total_laid_eggs=models.Sum("laid_eggs"),
            total_broken_eggs=models.Sum("broken_eggs"),
            total_dead_chickens=models.Sum("dead_chickens"),
            average_productivity=models.Avg("productivity"),
        )

        farm_resource = FarmResource.get_solo()
        statistics["total_remaining_eggs"] = farm_resource.eggs_count
        statistics["total_chickens"] = farm_resource.chickens_count

        sales = SalesReportFilter(request.GET, queryset=FarmSalesReport.objects.all()).qs
        sales_statistics = sales.aggregate(
            total_sold_eggs=models.Sum("sold_eggs"),
            total_cash_payment=models.Sum("cash_payment"),
            total_card_payment=models.Sum("card_payment"),
            total_debt_payment=models.Sum("debt_payment"),
            average_price=models.Avg("price_per_box"),
        )
        sales_statistics["total_payment"] = (
            sales_statistics["total_cash_payment"]
            + sales_statistics["total_card_payment"]
            + sales_statistics["total_debt_payment"]
        )

        statistics.update(sales_statistics)

        return Response(statistics, status=status.HTTP_200_OK)


__all__ = ["IncomeStatisticsAPIView"]
