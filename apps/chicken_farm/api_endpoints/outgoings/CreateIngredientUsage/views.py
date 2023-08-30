from rest_framework.generics import CreateAPIView

from apps.chicken_farm.models import FarmExpense
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import CreateIngredientUsageSerializer


class CreateIngredientUsageAPIView(CreateAPIView):
    queryset = FarmExpense.objects.all()
    serializer_class = CreateIngredientUsageSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


__all__ = ["CreateIngredientUsageAPIView"]
