from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.chicken_farm.choices import FarmDebtPaybackType
from apps.common.choices import DebtPaybackMethod
from apps.common.models import TimeStampedModel


class FarmDebtPayback(TimeStampedModel):
    expense = models.ForeignKey(
        verbose_name=_("expense"),
        to="chicken_farm.FarmExpense",
        on_delete=models.CASCADE,
        related_name="debt_paybacks",
        null=True,
        blank=True,
    )
    sales_report = models.ForeignKey(
        verbose_name=_("Sales report"),
        to="chicken_farm.FarmSalesReport",
        on_delete=models.CASCADE,
        related_name="debt_paybacks",
        null=True,
        blank=True,
    )
    type = models.CharField(verbose_name=_("Type"), max_length=15, choices=FarmDebtPaybackType.choices)
    amount = models.DecimalField(verbose_name=_("Money amount"), max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(
        verbose_name=_("Payment method"), max_length=15, choices=DebtPaybackMethod.choices
    )
    paid_at = models.DateTimeField(verbose_name=_("paid at"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("Debt payback")
        verbose_name_plural = _("Debt paybacks")

    def __str__(self):
        return f"#{self.id} - {self.type}"
