from django.urls import path

from .api_endpoints import CreateDailyReportAPIView

app_name = "chicken_farm"

urlpatterns = [
    path("daily-report/create/", CreateDailyReportAPIView.as_view(), name="create-daily-report"),
]
