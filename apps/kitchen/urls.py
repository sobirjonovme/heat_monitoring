from django.urls import path

from .api_endpoints import (OrderCreateAPIView, OrderDeliverAPIView,
                            ProductListAPIView)

app_name = "kitchen"

urlpatterns = [
    path("products/list/", ProductListAPIView.as_view(), name="product-list"),
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("order/deliver/", OrderDeliverAPIView.as_view(), name="order-deliver"),
]
