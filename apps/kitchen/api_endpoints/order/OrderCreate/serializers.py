from rest_framework import serializers

from apps.kitchen.models import Order, OrderItem


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "needed_quantity",
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "items",
        )
        extra_kwargs = {
            "status": {"read_only": True},
        }

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
