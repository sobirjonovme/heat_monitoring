from rest_framework.generics import ListAPIView

from apps.kitchen.models import Product

from .serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        queryset = queryset.select_related("unit")
        queryset = queryset.order_by("order")
        return queryset


__all__ = ["ProductListAPIView"]
