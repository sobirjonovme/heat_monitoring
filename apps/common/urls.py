from django.urls import path

from .api_endpoints import BuiltHelperAPIView

app_name = "common"

urlpatterns = [
    path("built-helper/", BuiltHelperAPIView.as_view(), name="built-helper"),
]
