import json

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.chicken_farm.models import FarmExpense

from .serializers import CreateFarmExpenseSerializer


class CreateFarmExpenseAPIView(CreateAPIView):
    queryset = FarmExpense.objects.all()
    serializer_class = CreateFarmExpenseSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        ex_type = data.get("type")
        data["type"] = json.loads(ex_type)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


__all__ = ["CreateFarmExpenseAPIView"]
