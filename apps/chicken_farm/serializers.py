from rest_framework import serializers

from apps.chicken_farm.models import FarmExpenseType


class FarmExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmExpenseType
        fields = ("id", "name")
