from django.urls import path

from .api_endpoints import (ActiveOrderDetailAPIView, OrderCheckAPIView,
                            OrderCreateAPIView, OrderDeliverAPIView,
                            OrderListAPIView, ProductListAPIView)

app_name = "kitchen"

urlpatterns = [
    path("products/list/", ProductListAPIView.as_view(), name="product-list"),
    # orders
    path("order/active/", ActiveOrderDetailAPIView.as_view(), name="order-active"),
    path("order/list/", OrderListAPIView.as_view(), name="order-list"),
    # order actions
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("order/deliver/", OrderDeliverAPIView.as_view(), name="order-deliver"),
    path("order/check/", OrderCheckAPIView.as_view(), name="order-check"),
]
