from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.chicken_farm.filters import DailyReportFilter
from apps.chicken_farm.models import FarmDailyReport
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import DailyReportListSerializer


class DailyReportListAPIView(ListAPIView):
    queryset = FarmDailyReport.objects.all().order_by("-date")
    serializer_class = DailyReportListSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = DailyReportFilter


__all__ = ["DailyReportListAPIView"]
