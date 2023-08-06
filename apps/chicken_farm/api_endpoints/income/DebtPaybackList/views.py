from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmIncomeDebtPayback
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .filters import IncomeDebtPaybackFilter
from .serializers import DebtPaybackListSerializer


class IncomeDebtPaybackListAPIView(ListAPIView):
    queryset = FarmIncomeDebtPayback.objects.all()
    serializer_class = DebtPaybackListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = IncomeDebtPaybackFilter


__all__ = ["IncomeDebtPaybackListAPIView"]
