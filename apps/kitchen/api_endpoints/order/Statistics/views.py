from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order, OrderItem, Product

from .serializers import DateRangeSerializer


class StatisticsAPIView(APIView):
    def get(self, request, *args, **kwargs):

        orders = Order.objects.exclude(status=OrderStatus.NEW)

        # check if data filter values are valid
        serializer = DateRangeSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        # get start_data and end_date from serializer
        start_date = serializer.validated_data.get("start_date")
        end_date = serializer.validated_data.get("end_date")

        if start_date:
            orders = orders.filter(created_at__gte=start_date)
        if end_date:
            orders = orders.filter(created_at__lte=end_date)

        data = orders.aggregate(
            total_money=Sum("items__price"),
        )

        for product in Product.objects.all():
            product_items = OrderItem.objects.filter(product=product, order__in=orders)
            if product_items.exists():
                data[product.name] = product_items.aggregate(
                    total_delivered_quantity=Sum("delivered_quantity"),
                    total_price=Sum("price"),
                )

        return Response(data, status=status.HTTP_200_OK)


__all__ = ["StatisticsAPIView"]
