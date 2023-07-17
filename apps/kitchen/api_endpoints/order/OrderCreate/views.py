from rest_framework.generics import CreateAPIView

from apps.kitchen.models import Order
from apps.kitchen.permissions import IsCookOrAdmin

from .serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsCookOrAdmin,)

    def perform_create(self, serializer):
        serializer.save(ordered_by=self.request.user)
