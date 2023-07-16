from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.kitchen.models import Order

from .serializers import OrderCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(ordered_by=self.request.user)
