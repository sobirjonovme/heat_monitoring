from rest_framework import serializers

from apps.chicken_farm.models import (FarmDebtPayback, FarmExpense,
                                      FarmSalesReport)


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmSalesReport
        fields = (
            "id",
            "comment",
            "sold_at",
        )
        ref_name = "FarmDebtPaybackSalesReportSerializer"


class ExpenseSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source="type.name", read_only=True)

    class Meta:
        model = FarmExpense
        fields = (
            "id",
            "type_name",
            "item_amount",
            "image",
            "date",
        )
        ref_name = "FarmDebtPaybackExpenseSerializer"


class FarmDebtPaybackListSerializer(serializers.ModelSerializer):
    sales_report = SalesReportSerializer(read_only=True)
    expense = ExpenseSerializer(read_only=True)

    class Meta:
        model = FarmDebtPayback
        fields = (
            "id",
            "sales_report",
            "expense",
            "type",
            "amount",
            "payment_method",
            "paid_at",
        )
