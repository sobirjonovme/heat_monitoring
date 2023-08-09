from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chicken_farm.models import FarmExpense, FarmSalesReport

from .serializers import ExpenseTypeStatisticsSerializer


class OverallStatisticsView(APIView):
    serializer_class = ExpenseTypeStatisticsSerializer

    def get(self, request, *args, **kwargs):
        statistics = {}

        sales = FarmSalesReport.objects.all()
        for sale in sales:
            date = sale.sold_at.date()
            if statistics.get(date):
                statistics[date]["income"] += sale.total_payment
                continue
            statistics[date] = {"income": sale.total_payment, "expenses": 0, "date": date}

        expenses = FarmExpense.objects.all()
        for expense in expenses:
            date = expense.date
            if statistics.get(date):
                statistics[date]["expenses"] += expense.total_payment
                continue
            statistics[date] = {"income": 0, "expenses": expense.total_payment, "date": date}

        return Response(statistics.values(), status=status.HTTP_200_OK)


__all__ = ["OverallStatisticsView"]
