# from django.db import models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chicken_farm.models import FarmDailyReport, FarmSalesReport

# from apps.chicken_farm.utils.daily_reports_update import \
#     bulk_update_daily_reports


class HelperAPIView(APIView):
    def get(self, request, format=None):
        # sales_reports = FarmDailyReport.objects.all().order_by("date")
        # target = sales_reports[1]
        # print(target)
        a = FarmSalesReport.objects.all()
        # bulk_update_daily_reports(target)

        # print(f'\n{a.values_list("sold_egg_boxes", flat=True)}\n')
        # a = models.Sum(a.values_list("sold_egg_boxes", flat=True))
        # print(f"\n\n\tSold egg boxes: {a}\n\n")
        print("\n\nbefore annotate\n\n")
        daily_reports = FarmDailyReport.objects.all().annotate_sold_egg_boxes()
        print("\n\nafter annotate\n\n")
        print(daily_reports)
        print("\n\nbefore for\n\n")
        for a in daily_reports:
            print(a.cnt)

        return Response(status=status.HTTP_200_OK)


__all__ = ["HelperAPIView"]
