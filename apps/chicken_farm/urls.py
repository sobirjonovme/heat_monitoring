from django.urls import path

from .api_endpoints import (CreateDailyReportAPIView, CreateDebtPaybackAPIView,
                            CreateFarmExpenseAPIView, CreateSalesReportAPIView,
                            DailyReportListAPIView, DebtPaybackListAPIView,
                            IncomeStatisticsAPIView, SalesReportListAPIView)

app_name = "chicken_farm"

urlpatterns = [
    # daily report
    path("daily-report/create/", CreateDailyReportAPIView.as_view(), name="create-daily-report"),
    path("daily-report/list/", DailyReportListAPIView.as_view(), name="list-daily-report"),
    # sales report
    path("sales-report/create/", CreateSalesReportAPIView.as_view(), name="create-sales-report"),
    path("sales-report/list/", SalesReportListAPIView.as_view(), name="list-sales-report"),
    # farm expenses
    path("farm-expense/create/", CreateFarmExpenseAPIView.as_view(), name="create-farm-expense"),
    # farm common
    path("income-statistics/", IncomeStatisticsAPIView.as_view(), name="income-statistics"),
    path("debt-payback/create/", CreateDebtPaybackAPIView.as_view(), name="create-debt-payback"),
    path("debt-payback/list/", DebtPaybackListAPIView.as_view(), name="list-debt-payback"),
]
