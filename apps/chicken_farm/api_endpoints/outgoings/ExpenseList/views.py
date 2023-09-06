from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView

from apps.chicken_farm.filters import FarmExpenseFilter
from apps.chicken_farm.models import FarmExpense
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import FarmExpenseListSerializer


class FarmExpenseListAPIView(ListAPIView):
    serializer_class = FarmExpenseListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FarmExpenseFilter

    def get_queryset(self):
        queryset = FarmExpense.objects.all().order_by("-date")
        queryset = queryset.select_related("type")
        return queryset


__all__ = ["FarmExpenseListAPIView"]
