from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.chicken_farm.models import FarmSalesReport
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .filters import SalesReportFilter
from .serializers import SalesReportListSerializer


class SalesReportListAPIView(ListAPIView):
    queryset = FarmSalesReport.objects.all().order_by("-sold_at")
    serializer_class = SalesReportListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = SalesReportFilter


__all__ = ["SalesReportListAPIView"]
