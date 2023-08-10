from django_filters import rest_framework as filters

from apps.chicken_farm.models import (FarmDailyReport, FarmExpense,
                                      FarmSalesReport)


class DailyReportFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = FarmDailyReport
        fields = ("from_date", "to_date")


class SalesReportFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="sold_at", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="sold_at", lookup_expr="lte")

    class Meta:
        model = FarmSalesReport
        fields = ("from_date", "to_date")


class FarmExpenseFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = FarmExpense
        fields = ("from_date", "to_date", "type")
