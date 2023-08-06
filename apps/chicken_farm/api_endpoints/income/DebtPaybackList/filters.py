from django_filters import rest_framework as filters

from apps.chicken_farm.models import FarmIncomeDebtPayback


class IncomeDebtPaybackFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="paid_at", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="paid_at", lookup_expr="lte")

    class Meta:
        model = FarmIncomeDebtPayback
        fields = (
            "from_date",
            "to_date",
        )
