from django.db import models
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chicken_farm.filters import DATE_FILTER_PARAMETERS, FarmExpenseFilter
from apps.chicken_farm.models import FarmExpense
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin


class OutgoingsStatisticsAPIView(APIView):
    permission_classes = (IsFarmCounterOrAdmin,)

    @swagger_auto_schema(manual_parameters=DATE_FILTER_PARAMETERS)
    def get(self, request, *args, **kwargs):
        queryset = FarmExpense.objects.all()
        filtered_queryset = FarmExpenseFilter(request.GET, queryset=queryset).qs

        statistics = filtered_queryset.aggregate(
            total_card_payment=models.Sum("card_payment"),
            total_cash_payment=models.Sum("cash_payment"),
            total_debt_payment=models.Sum("debt_payment"),
        )

        statistics["total_payment"] = (
            statistics["total_card_payment"] + statistics["total_cash_payment"] + statistics["total_debt_payment"]
        )

        return Response(statistics, status=status.HTTP_200_OK)


__all__ = ["OutgoingsStatisticsAPIView"]
