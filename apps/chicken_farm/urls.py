from django.urls import path

from .api_endpoints import (CreateDailyReportAPIView,
                            CreateIncomeDebtPaybackAPIView,
                            CreateSalesReportAPIView, DailyReportListAPIView,
                            FarmStatisticsAPIView,
                            IncomeDebtPaybackListAPIView,
                            SalesReportListAPIView)

app_name = "chicken_farm"

urlpatterns = [
    # daily report
    path("daily-report/create/", CreateDailyReportAPIView.as_view(), name="create-daily-report"),
    path("daily-report/list/", DailyReportListAPIView.as_view(), name="list-daily-report"),
    # sales report
    path("sales-report/create/", CreateSalesReportAPIView.as_view(), name="create-sales-report"),
    path("sales-report/list/", SalesReportListAPIView.as_view(), name="list-sales-report"),
    # income debt payback
    path("income-debt-payback/create/", CreateIncomeDebtPaybackAPIView.as_view(), name="create-income-debt-payback"),
    path("income-debt-payback/list/", IncomeDebtPaybackListAPIView.as_view(), name="list-income-debt-payback"),
    # farm statistics
    path("farm-statistics/", FarmStatisticsAPIView.as_view(), name="farm-statistics"),
]
