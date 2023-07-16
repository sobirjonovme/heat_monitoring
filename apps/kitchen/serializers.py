from rest_framework import serializers

from apps.kitchen.models import ProductUnit


class ProductUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = ("id", "name", "short_name")
