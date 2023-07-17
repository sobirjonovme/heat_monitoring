from django.db import models
from rest_framework import serializers

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order, OrderItem, Product, ProductUnit
from apps.users.models import User


class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = ("id", "name", "short_name")


class OrderDetailProductSerializer(serializers.ModelSerializer):
    unit = ProductUnitSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "unit",
        )


class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "role",
        )


class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = OrderDetailProductSerializer(read_only=True)
    checked_by = OrderUserSerializer(read_only=True)
    quantity_difference = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "order",
            "product",
            "needed_quantity",
            "delivered_quantity",
            "price",
            "quantity_difference",
            "is_checked",
            "checked_by",
        )


class OrderDetailSerializer(serializers.ModelSerializer):
    ordered_by = OrderUserSerializer(read_only=True)
    delivered_by = OrderUserSerializer(read_only=True)
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "items",
            "ordered_by",
            "delivered_by",
            "created_at",
        )

    def get_items(self, obj):
        items = obj.items.all()
        if obj.status == OrderStatus.NEW:
            # give None value to quantity_difference field
            items = items.annotate(quantity_difference=models.Value(None, output_field=models.DecimalField()))
        else:
            items = items.annotate(quantity_difference=models.F("delivered_quantity") - models.F("needed_quantity"))
        return OrderItemDetailSerializer(items, many=True).data
