from django.urls import path

from .api_endpoints import (ActiveOrderDetailAPIView, OrderCreateAPIView,
                            OrderDeliverAPIView, OrderListAPIView,
                            ProductListAPIView)

app_name = "kitchen"

urlpatterns = [
    path("products/list/", ProductListAPIView.as_view(), name="product-list"),
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("order/deliver/", OrderDeliverAPIView.as_view(), name="order-deliver"),
    path("order/active/", ActiveOrderDetailAPIView.as_view(), name="order-active"),
    path("order/list/", OrderListAPIView.as_view(), name="order-list"),
]
