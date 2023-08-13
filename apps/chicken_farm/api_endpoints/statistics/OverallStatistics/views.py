from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chicken_farm.filters import (DATE_FILTER_PARAMETERS,
                                       FarmExpenseFilter, SalesReportFilter)
from apps.chicken_farm.models import FarmExpense, FarmSalesReport
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin


class OverallStatisticsView(APIView):
    permission_classes = (IsFarmCounterOrAdmin,)

    @swagger_auto_schema(manual_parameters=DATE_FILTER_PARAMETERS)
    def get(self, request, *args, **kwargs):
        statistics = {}

        sales = SalesReportFilter(request.GET, queryset=FarmSalesReport.objects.all()).qs
        for sale in sales:
            date = sale.sold_at.date()
            if statistics.get(date):
                statistics[date]["income"] += sale.total_payment
                continue
            statistics[date] = {"income": sale.total_payment, "expenses": 0, "date": date}

        expenses = FarmExpenseFilter(request.GET, queryset=FarmExpense.objects.all()).qs
        for expense in expenses:
            date = expense.date
            if statistics.get(date):
                statistics[date]["expenses"] += expense.total_payment
                continue
            statistics[date] = {"income": 0, "expenses": expense.total_payment, "date": date}

        # sort by date
        statistics = statistics.values()
        statistics = sorted(statistics, key=lambda x: x["date"])

        return Response(statistics, status=status.HTTP_200_OK)


__all__ = ["OverallStatisticsView"]
