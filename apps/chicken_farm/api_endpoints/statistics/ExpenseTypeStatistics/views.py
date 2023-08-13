from django.db import models
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView

from apps.chicken_farm.filters import DATE_FILTER_PARAMETERS, FarmExpenseFilter
from apps.chicken_farm.models import FarmExpense, FarmExpenseType
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import ExpenseTypeStatisticsSerializer


class ExpenseTypeStatisticsView(ListAPIView):
    queryset = FarmExpenseType.objects.all()
    serializer_class = ExpenseTypeStatisticsSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    @swagger_auto_schema(manual_parameters=DATE_FILTER_PARAMETERS)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        expense_queryset = FarmExpense.objects.filter(type_id=models.OuterRef("id")).annotate(
            total_payment=models.F("card_payment") + models.F("cash_payment") + models.F("debt_payment")
        )
        filtered_expense_queryset = FarmExpenseFilter(self.request.GET, queryset=expense_queryset).qs

        queryset = self.queryset.annotate(total_expenses=models.Sum(filtered_expense_queryset.values("total_payment")))
        return queryset.filter(total_expenses__gt=0)


__all__ = ["ExpenseTypeStatisticsView"]
