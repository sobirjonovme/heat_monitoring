from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.kitchen.models import Order
from apps.kitchen.serializers import OrderDetailSerializer


class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["OrderDetailAPIView"]
