from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmFodderIngredientUsage
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .filters import FarmFodderIngredientUsageFilter
from .serializers import IngredientUsageListSerializer


class FarmFodderIngredientUsageListAPIView(ListAPIView):
    serializer_class = IngredientUsageListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FarmFodderIngredientUsageFilter

    def get_queryset(self):
        queryset = FarmFodderIngredientUsage.objects.all().order_by("-date")
        queryset = queryset.select_related("ingredient")
        return queryset


__all__ = ["FarmFodderIngredientUsageListAPIView"]
