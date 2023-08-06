from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel


class FarmExpenseType(TimeStampedModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    class Meta:
        verbose_name = _("expense type")
        verbose_name_plural = _("expense types")

    def __str__(self):
        return self.name


class FarmExpense(TimeStampedModel):
    type = models.ForeignKey(
        verbose_name=_("type"), to="chicken_farm.FarmExpenseType", on_delete=models.CASCADE, related_name="expenses"
    )
    card_payment = models.DecimalField(verbose_name=_("Card money"), max_digits=10, decimal_places=2, default=0)
    cash_payment = models.DecimalField(verbose_name=_("Cash money"), max_digits=10, decimal_places=2, default=0)
    debt_payment = models.DecimalField(verbose_name=_("Debt money"), max_digits=10, decimal_places=2, default=0)
    image = ImageField(verbose_name=_("image"), upload_to="expenses", null=True, blank=True)
    date = models.DateField(verbose_name=_("date"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("expense")
        verbose_name_plural = _("expenses")

    def __str__(self):
        return f"#{self.id} - {self.type}"


class FarmOutgoingsDebtPayback(TimeStampedModel):
    expense = models.ForeignKey(
        verbose_name=_("expense"), to="chicken_farm.FarmExpense", on_delete=models.CASCADE, related_name="debt_paybacks"
    )
    card_payment = models.DecimalField(verbose_name=_("Card money"), max_digits=10, decimal_places=2, default=0)
    cash_payment = models.DecimalField(verbose_name=_("Cash money"), max_digits=10, decimal_places=2, default=0)
    paid_at = models.DateTimeField(verbose_name=_("paid at"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )
