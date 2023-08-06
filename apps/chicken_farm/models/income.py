from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from apps.common.models import TimeStampedModel


# Create your models here.
class FarmResource(SingletonModel, TimeStampedModel):
    chickens_count = models.PositiveIntegerField(verbose_name=_("chickens count"), default=0)
    eggs_count = models.PositiveIntegerField(verbose_name=_("eggs count"), default=0)

    class Meta:
        verbose_name = "farm resource"
        verbose_name_plural = "farm resource"

    def __str__(self):
        return str(_("Farm Resource"))


class FarmDailyReport(TimeStampedModel):
    laid_eggs = models.PositiveIntegerField(verbose_name=_("laid eggs"), default=0)
    broken_eggs = models.PositiveIntegerField(verbose_name=_("broken eggs"), default=0)
    dead_chickens = models.PositiveIntegerField(verbose_name=_("dead chickens"), default=0)
    total_remaining_eggs = models.PositiveIntegerField(verbose_name=_("total remaining eggs"), null=True, blank=True)
    remaining_chickens = models.PositiveIntegerField(verbose_name=_("remaining chickens"), null=True, blank=True)
    productivity = models.FloatField(verbose_name=_("productivity"), null=True, blank=True)
    date = models.DateField(verbose_name=_("date"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("daily report")
        verbose_name_plural = _("daily reports")

    def __str__(self):
        return f"#{self.id} - {self.date}"


class FarmSalesReport(TimeStampedModel):
    sold_eggs = models.PositiveIntegerField(verbose_name=_("sold eggs"), default=0, help_text=_("sold eggs in boxes"))
    price_per_box = models.PositiveIntegerField(verbose_name=_("price per box"), default=0)
    comment = models.TextField(verbose_name=_("comments"), null=True, blank=True)
    card_payment = models.DecimalField(verbose_name=_("Card money"), max_digits=10, decimal_places=2, default=0)
    cash_payment = models.DecimalField(verbose_name=_("Cash money"), max_digits=10, decimal_places=2, default=0)
    debt_payment = models.DecimalField(verbose_name=_("Debt money"), max_digits=10, decimal_places=2, default=0)
    sold_at = models.DateTimeField(verbose_name=_("sold at"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("sales report")
        verbose_name_plural = _("sales reports")

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f"#{self.id} - {self.sold_at}"

    @property
    def total_payment(self):
        return self.cash_payment + self.card_payment + self.debt_payment


class FarmIncomeDebtPayback(TimeStampedModel):
    sales_report = models.ForeignKey(
        verbose_name=_("Sales report"),
        to="chicken_farm.FarmSalesReport",
        on_delete=models.CASCADE,
        related_name="debt_paybacks",
    )
    card_payment = models.DecimalField(verbose_name=_("Card money"), max_digits=10, decimal_places=2, default=0)
    cash_payment = models.DecimalField(verbose_name=_("Cash money"), max_digits=10, decimal_places=2, default=0)
    paid_at = models.DateTimeField(verbose_name=_("paid at"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("income debt payback")
        verbose_name_plural = _("income debt paybacks")

    def __str__(self):
        return f"#{self.id} - {self.paid_at}"
