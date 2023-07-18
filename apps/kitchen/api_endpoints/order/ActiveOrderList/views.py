from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order
from apps.kitchen.serializers import OrderDetailSerializer
from apps.users.models import UserRoles


class ActiveOrderListAPIView(ListAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == UserRoles.PROVIDER:
            return Order.objects.filter(status=OrderStatus.NEW)

        if user.role == UserRoles.COOK:
            return Order.objects.exclude(status=OrderStatus.CHECKED)

        if user.role == UserRoles.ADMIN:
            return Order.objects.exclude(status=OrderStatus.CHECKED)


__all__ = ["ActiveOrderListAPIView"]
