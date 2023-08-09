from rest_framework import serializers

from apps.chicken_farm.models import FarmExpenseType


class ExpenseTypeStatisticsSerializer(serializers.ModelSerializer):
    total_expenses = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = FarmExpenseType
        fields = ("id", "name", "total_expenses")
