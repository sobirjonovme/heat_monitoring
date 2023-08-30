from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmExpenseType
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin
from apps.chicken_farm.serializers import FarmExpenseTypeSerializer


class FarmExpenseTypeListAPIView(ListAPIView):
    queryset = FarmExpenseType.objects.all().order_by("name")
    serializer_class = FarmExpenseTypeSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    pagination_class = None
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ("category",)
    search_fields = ("name",)


__all__ = ["FarmExpenseTypeListAPIView"]
