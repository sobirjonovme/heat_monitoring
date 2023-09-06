from django_filters import rest_framework as filters

from apps.chicken_farm.models import FarmFodderIngredientUsage


class FarmFodderIngredientUsageFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = FarmFodderIngredientUsage
        fields = ("from_date", "to_date", "ingredient")
