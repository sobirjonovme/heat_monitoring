from rest_framework.generics import CreateAPIView

from apps.chicken_farm.models import FarmExpense

from .serializers import CreateFarmExpenseSerializer


class CreateFarmExpenseAPIView(CreateAPIView):
    queryset = FarmExpense.objects.all()
    serializer_class = CreateFarmExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)


__all__ = ["CreateFarmExpenseAPIView"]
