from rest_framework import serializers

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order, OrderItem


class OrderItemDeliverSerializer(serializers.Serializer):
    order_item_id = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all())
    delivered_quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class OrderDeliverSerializer(serializers.Serializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    items = OrderItemDeliverSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "order_id",
            "items",
        )

    def validate_order(self, value):
        if value.status != OrderStatus.NEW:
            raise serializers.ValidationError(
                detail={"order": "Order already delivered."},
                code="invalid",
            )
        return value
