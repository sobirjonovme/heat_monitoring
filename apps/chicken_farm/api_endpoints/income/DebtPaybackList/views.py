from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmIncomeDebtPayback
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import DebtPaybackListSerializer


class IncomeDebtPaybackListAPIView(ListAPIView):
    queryset = FarmIncomeDebtPayback.objects.all()
    serializer_class = DebtPaybackListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)


__all__ = ["IncomeDebtPaybackListAPIView"]
