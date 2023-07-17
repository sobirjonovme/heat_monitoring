from django.db.models import Case, DecimalField, Sum, Value, When
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.kitchen.choices import OrderStatus
from apps.kitchen.models import Order
from apps.users.models import UserRoles

from .serializers import OrderListSerializer


class OrderListAPIView(ListAPIView):
    serializer_class = OrderListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        if user.role == UserRoles.PROVIDER:
            queryset = user.delivered_orders.all()

        if user.role == UserRoles.COOK:
            queryset = user.created_orders.all()

        if user.role == UserRoles.ADMIN:
            queryset = Order.objects.all()

        # if object status CHECKED, then annotate total_money
        # in other cases, annotate total_money = 0
        # total money = sum of all items' prices
        queryset = queryset.annotate(
            total_money=Sum(
                Case(
                    When(status=OrderStatus.CHECKED, then="items__price"),  # Calculate sum only if status is 'done'
                    default=Value(0),  # Default value of total_money when status is not 'done'
                    output_field=DecimalField(),  # Specify the output field type
                )
            )
        )
        return queryset


__all__ = ["OrderListAPIView"]
