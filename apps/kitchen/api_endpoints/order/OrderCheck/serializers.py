from rest_framework import serializers

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order, OrderItem


class OrderItemCheckSerializer(serializers.Serializer):
    order_item_id = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all())
    is_checked = serializers.BooleanField(required=True)


class OrderCheckSerializer(serializers.Serializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    items = OrderItemCheckSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "order_id",
            "items",
        )

    def validate_order(self, value):
        if value.status != OrderStatus.DELIVERED:
            raise serializers.ValidationError(
                detail={"order": "Order is not delivered yet."},
                code="invalid",
            )
        return value
