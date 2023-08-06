from django.urls import path

from .api_endpoints import (CreateDailyReportAPIView, CreateSalesReportAPIView,
                            DailyReportListAPIView, FarmStatisticsAPIView)

app_name = "chicken_farm"

urlpatterns = [
    # daily report
    path("daily-report/create/", CreateDailyReportAPIView.as_view(), name="create-daily-report"),
    path("daily-report/list/", DailyReportListAPIView.as_view(), name="list-daily-report"),
    # sales report
    path("sales-report/create/", CreateSalesReportAPIView.as_view(), name="create-sales-report"),
    # farm statistics
    path("farm-statistics/", FarmStatisticsAPIView.as_view(), name="farm-statistics"),
]
