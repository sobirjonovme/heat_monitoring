from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmExpense

from .filters import FarmExpenseFilter
from .serializers import FarmExpenseListSerializer


class FarmExpenseListAPIView(ListAPIView):
    queryset = FarmExpense.objects.all()
    serializer_class = FarmExpenseListSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FarmExpenseFilter


__all__ = ["FarmExpenseListAPIView"]
