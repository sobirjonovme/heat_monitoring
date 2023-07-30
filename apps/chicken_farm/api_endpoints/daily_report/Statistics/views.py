from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.chicken_farm.filters import DailyReportFilter
from apps.chicken_farm.models import DailyReport, FarmResource
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin


class FarmStatisticsAPIView(GenericAPIView):
    queryset = DailyReport.objects.all()
    permission_classes = (IsFarmCounterOrAdmin,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = DailyReportFilter

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        statistics = queryset.aggregate(
            total_laid_eggs=models.Sum("laid_eggs"),
            total_broken_eggs=models.Sum("broken_eggs"),
            total_sold_eggs=models.Sum("sold_eggs"),
            total_dead_chickens=models.Sum("dead_chickens"),
            average_productivity=models.Avg("productivity"),
        )

        farm_resource = FarmResource.get_solo()
        statistics["total_remaining_eggs"] = farm_resource.eggs_count
        statistics["total_chickens"] = farm_resource.chickens_count

        return Response(statistics, status=status.HTTP_200_OK)


__all__ = ["FarmStatisticsAPIView"]
