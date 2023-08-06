from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView

from apps.chicken_farm.models import FarmDailyReport
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import CreateDailyReportSerializer


class CreateDailyReportAPIView(CreateAPIView):
    queryset = FarmDailyReport.objects.all()
    serializer_class = CreateDailyReportSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    def post(self, request, *args, **kwargs):
        # get today
        today = timezone.now().date()

        # check if the report has not already been submitted today
        if FarmDailyReport.objects.filter(date=today).exists():
            raise ValidationError(code="already_submitted", detail=_("You have already submitted a report for today."))

        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


__all__ = ["CreateDailyReportAPIView"]
