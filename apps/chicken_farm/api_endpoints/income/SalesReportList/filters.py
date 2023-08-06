from django_filters import rest_framework as filters

from apps.chicken_farm.models import FarmSalesReport


class SalesReportFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="sold_at", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="sold_at", lookup_expr="lte")

    class Meta:
        model = FarmSalesReport
        fields = ("from_date", "to_date")
