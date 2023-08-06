from rest_framework.generics import CreateAPIView

from apps.chicken_farm.models import FarmIncomeDebtPayback
from apps.chicken_farm.permissions import IsFarmCounterOrAdmin

from .serializers import CreateDebtPaybackSerializer


class CreateIncomeDebtPaybackAPIView(CreateAPIView):
    queryset = FarmIncomeDebtPayback.objects.all()
    serializer_class = CreateDebtPaybackSerializer
    permission_classes = (IsFarmCounterOrAdmin,)

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


__all__ = ["CreateIncomeDebtPaybackAPIView"]
