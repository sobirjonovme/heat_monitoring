from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .api_endpoints import CustomTokenObtainPairView, MyProfileAPIView

app_name = "users"

urlpatterns = [
    path("token/", CustomTokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("profile/", MyProfileAPIView.as_view(), name="my-profile"),
]
