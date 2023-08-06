from rest_framework.generics import CreateAPIView

from apps.chicken_farm.models import FarmDailyReport
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import CreateSalesReportSerializer


class CreateSalesReportAPIView(CreateAPIView):
    queryset = FarmDailyReport.objects.all()
    serializer_class = CreateSalesReportSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


__all__ = ["CreateSalesReportAPIView"]
