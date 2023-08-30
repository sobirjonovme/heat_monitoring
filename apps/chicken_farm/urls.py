from django.urls import path

from .api_endpoints import (CreateDailyReportAPIView, CreateDebtPaybackAPIView,
                            CreateFarmExpenseAPIView,
                            CreateIngredientUsageAPIView,
                            CreateSalesReportAPIView, DailyReportListAPIView,
                            DebtPaybackListAPIView, ExpenseTypeStatisticsView,
                            FarmExpenseListAPIView, FarmExpenseTypeListAPIView,
                            HelperAPIView, IncomeStatisticsAPIView,
                            OutgoingsStatisticsAPIView, OverallStatisticsView,
                            SalesReportListAPIView)

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
    path("ingredient-usage/create/", CreateIngredientUsageAPIView.as_view(), name="create-ingredient-usage"),
    path("farm-expense/list/", FarmExpenseListAPIView.as_view(), name="list-farm-expense"),
    path("farm-expense-type/list/", FarmExpenseTypeListAPIView.as_view(), name="list-farm-expense-type"),
    # statistics
    path("expense-type-statistics/", ExpenseTypeStatisticsView.as_view(), name="expense-type-statistics"),
    path("overall-statistics/", OverallStatisticsView.as_view(), name="overall-statistics"),
    path("income-statistics/", IncomeStatisticsAPIView.as_view(), name="income-statistics"),
    path("outgoings-statistics/", OutgoingsStatisticsAPIView.as_view(), name="outgoings-statistics"),
    # farm common
    path("debt-payback/create/", CreateDebtPaybackAPIView.as_view(), name="create-debt-payback"),
    path("debt-payback/list/", DebtPaybackListAPIView.as_view(), name="list-debt-payback"),
    path("helper/", HelperAPIView.as_view(), name="helper"),
]
