from django.urls import path

from .api_endpoints import OrderCreateAPIView, ProductListAPIView

app_name = "kitchen"

urlpatterns = [
    path("products/list/", ProductListAPIView.as_view(), name="product-list"),
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
]
