from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order
from apps.kitchen.serializers import OrderDetailSerializer
from apps.users.models import UserRoles


class ActiveOrderDetailAPIView(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        if user.role == UserRoles.PROVIDER:
            return user.delivered_orders.filter(status=OrderStatus.NEW).first()

        if user.role == UserRoles.COOK:
            return user.created_orders.exclude(status=OrderStatus.CHECKED).first()

        if user.role == UserRoles.ADMIN:
            return Order.objects.exclude(status=OrderStatus.CHECKED).first()


__all__ = ["ActiveOrderDetailAPIView"]
