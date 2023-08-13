from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmDebtPayback
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .filters import DebtPaybackFilter
from .serializers import FarmDebtPaybackListSerializer


class DebtPaybackListAPIView(ListAPIView):
    queryset = FarmDebtPayback.objects.all().order_by("-paid_at")
    serializer_class = FarmDebtPaybackListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = DebtPaybackFilter


__all__ = ["DebtPaybackListAPIView"]
