from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.chicken_farm.filters import FarmExpenseFilter
from apps.chicken_farm.models import FarmExpense
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin


class OutgoingsStatisticsAPIView(GenericAPIView):
    queryset = FarmExpense.objects.all()
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = FarmExpenseFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        statistics = queryset.aggregate(
            total_card_payment=models.Sum("card_payment"),
            total_cash_payment=models.Sum("cash_payment"),
            total_debt_payment=models.Sum("debt_payment"),
        )

        statistics["total_payment"] = (
            statistics["total_card_payment"] + statistics["total_cash_payment"] + statistics["total_debt_payment"]
        )

        return Response(statistics, status=status.HTTP_200_OK)


__all__ = ["OutgoingsStatisticsAPIView"]
