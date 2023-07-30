from django.urls import path

from .api_endpoints import (CreateDailyReportAPIView, DailyReportListAPIView,
                            FarmStatisticsAPIView)

app_name = "chicken_farm"

urlpatterns = [
    path("daily-report/create/", CreateDailyReportAPIView.as_view(), name="create-daily-report"),
    path("daily-report/list/", DailyReportListAPIView.as_view(), name="list-daily-report"),
    path("farm-statistics/", FarmStatisticsAPIView.as_view(), name="farm-statistics"),
]
