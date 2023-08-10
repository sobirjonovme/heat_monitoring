from django.db import models
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmExpense, FarmExpenseType
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import ExpenseTypeStatisticsSerializer


class ExpenseTypeStatisticsView(ListAPIView):
    queryset = FarmExpenseType.objects.all()
    serializer_class = ExpenseTypeStatisticsSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    def get_queryset(self):
        expense_queryset = FarmExpense.objects.filter(type_id=models.OuterRef("id")).annotate(
            total_payment=models.F("card_payment") + models.F("cash_payment") + models.F("debt_payment")
        )

        queryset = self.queryset.annotate(total_expenses=models.Sum(expense_queryset.values("total_payment")))
        return queryset.filter(total_expenses__gt=0)


__all__ = ["ExpenseTypeStatisticsView"]
