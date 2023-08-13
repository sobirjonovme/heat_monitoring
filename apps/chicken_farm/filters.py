from django_filters import rest_framework as filters
from drf_yasg import openapi

from apps.chicken_farm.models import (FarmDailyReport, FarmExpense,
                                      FarmSalesReport)


class DailyReportFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = FarmDailyReport
        fields = ("from_date", "to_date")


class SalesReportFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="sold_at__date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="sold_at__date", lookup_expr="lte")
    only_debt = filters.BooleanFilter(field_name="debt", method="filter_debt")

    class Meta:
        model = FarmSalesReport
        fields = ("from_date", "to_date", "only_debt")

    def filter_debt(self, queryset, name, value):
        if value:
            return queryset.filter(debt_payment__gt=0)
        return queryset


class FarmExpenseFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="date", lookup_expr="lte")
    only_debt = filters.BooleanFilter(field_name="debt", method="filter_debt")

    class Meta:
        model = FarmExpense
        fields = ("from_date", "to_date", "type", "only_debt")

    def filter_debt(self, queryset, name, value):
        if value:
            return queryset.filter(debt_payment__gt=0)
        return queryset


DATE_FILTER_PARAMETERS = [
    openapi.Parameter("from_date", openapi.IN_QUERY, type=openapi.FORMAT_DATE),
    openapi.Parameter("to_date", openapi.IN_QUERY, type=openapi.FORMAT_DATE),
]
