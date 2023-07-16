from rest_framework import serializers

from apps.kitchen.models import Product
from apps.kitchen.serializers import ProductUnitSerializer


class ProductListSerializer(serializers.Serializer):
    unit = ProductUnitSerializer()

    class Meta:
        model = Product
        fields = ("id", "name", "unit", "order", "is_active")
