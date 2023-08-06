from django.urls import path

from .api_endpoints import (ActiveOrderListAPIView, OrderCheckAPIView,
                            OrderCreateAPIView, OrderDeliverAPIView,
                            OrderDetailAPIView, OrderListAPIView,
                            ProductListAPIView, StatisticsAPIView)

app_name = "kitchen"

urlpatterns = [
    path("products/list/", ProductListAPIView.as_view(), name="product-list"),
    # orders
    path("order/list/active/", ActiveOrderListAPIView.as_view(), name="order-list-active"),
    path("order/list/", OrderListAPIView.as_view(), name="order-list"),
    path("order/<int:pk>/detail/", OrderDetailAPIView.as_view(), name="order-detail"),
    path("order/common/", StatisticsAPIView.as_view(), name="order-common"),
    # order actions
    path("order/create/", OrderCreateAPIView.as_view(), name="order-create"),
    path("order/deliver/", OrderDeliverAPIView.as_view(), name="order-deliver"),
    path("order/check/", OrderCheckAPIView.as_view(), name="order-check"),
]
