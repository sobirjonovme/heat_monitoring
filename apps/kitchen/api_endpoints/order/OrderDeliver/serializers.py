from rest_framework import serializers

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
            "status",
            "items",
        )
        extra_kwargs = {
            "status": {"read_only": True},
        }
