from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmDebtPayback
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .filters import DebtPaybackFilter
from .serializers import FarmDebtPaybackListSerializer


class DebtPaybackListAPIView(ListAPIView):
    queryset = FarmDebtPayback.objects.all()
    serializer_class = FarmDebtPaybackListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = DebtPaybackFilter

    def get_queryset(self):
        queryset = self.queryset.order_by("-paid_at")
        return queryset.select_related("sales_report", "expense", "expense__type")


__all__ = ["DebtPaybackListAPIView"]
