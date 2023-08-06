from django_filters import rest_framework as filters

from apps.chicken_farm.models import FarmDebtPayback


class DebtPaybackFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="paid_at", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="paid_at", lookup_expr="lte")

    class Meta:
        model = FarmDebtPayback
        fields = (
            "from_date",
            "to_date",
            "type",
        )
