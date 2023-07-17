from rest_framework import serializers

from apps.kitchen.models import Order
from apps.kitchen.serializers import OrderUserSerializer


class OrderListSerializer(serializers.ModelSerializer):
    ordered_by = OrderUserSerializer(read_only=True)
    delivered_by = OrderUserSerializer(read_only=True)
    total_money = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "ordered_by",
            "delivered_by",
            "total_money",
            "created_at",
        )
