from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView

from apps.kitchen.choices import OrderStatus

from .serializers import OrderDeliverSerializer


class OrderDeliverAPIView(APIView):
    serializer_class = OrderDeliverSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        order = data["order"]
        items = data["items"]

        for item in items:
            if item["order_item_id"].order != order:
                raise ValidationError(
                    detail={"order": "Order item does not belong to the order."},
                    code="invalid",
                )

        order.status = OrderStatus.DELIVERED
        order.delivered_by = request.user
        order.save()

        for item in items:
            order_item = item["order_item_id"]
            order_item.delivered_quantity = item.get("delivered_quantity")
            order_item.price = item.get("price")
            order_item.save()

        return Response(status=status.HTTP_200_OK)


__all__ = ["OrderDeliverAPIView"]
