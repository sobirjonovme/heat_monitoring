from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from apps.chicken_farm.choices import FarmDebtPaybackType
from apps.common.choices import DebtPaybackMethod
from apps.common.models import TimeStampedModel


class FarmResource(SingletonModel, TimeStampedModel):
    # current farm resource
    current_chickens_count = models.PositiveIntegerField(verbose_name=_("current chickens count"), default=0)
    current_eggs_count = models.PositiveIntegerField(verbose_name=_("current eggs count"), default=0)
    # initial farm resource
    initial_chickens_count = models.PositiveIntegerField(verbose_name=_("initial chickens count"), default=0)
    initial_eggs_count = models.PositiveIntegerField(verbose_name=_("initial eggs count"), default=0)

    class Meta:
        verbose_name = _("farm resource")
        verbose_name_plural = _("farm resource")

    def __str__(self):
        return str(_("Farm Resource"))

    @classmethod
    def update_according_to_last_report(cls, last_report=None):
        if not last_report:
            from apps.chicken_farm.models.income import FarmDailyReport

            last_report = FarmDailyReport.objects.order_by("-date").first()
        if last_report:
            farm_resource = cls.get_solo()
            farm_resource.current_chickens_count = last_report.remaining_chickens
            farm_resource.current_eggs_count = last_report.total_remaining_eggs
            farm_resource.save()


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
    amount = models.DecimalField(verbose_name=_("Money amount"), max_digits=12, decimal_places=2, default=0)
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

    def delete(self, using=None, keep_parents=False):
        self.unapply_to_report()
        return super().delete(using=using, keep_parents=keep_parents)

    def apply_to_report(self):
        # Update Expense or Sales Report according to this payback
        # reduce debt by amount, increase card or cash payment by amount

        # Check if this payback is via card or cash
        via_card = self.payment_method == DebtPaybackMethod.CARD
        via_cash = self.payment_method == DebtPaybackMethod.CASH

        # if Debt Payback is for expense
        if self.type == FarmDebtPaybackType.OUTGOINGS:
            if via_card:
                self.expense.card_payment += self.amount
            elif via_cash:
                self.expense.cash_payment += self.amount
            self.expense.debt_payment -= self.amount
            self.expense.save()

        # if Debt Payback is for sales
        elif self.type == FarmDebtPaybackType.INCOME:
            if via_card:
                self.sales_report.card_payment += self.amount
            elif via_cash:
                self.sales_report.cash_payment += self.amount
            self.sales_report.debt_payment -= self.amount
            self.sales_report.save()

    def unapply_to_report(self):
        # Back Sales Report or Expense to previous state, before applying this payback
        # increase debt by amount, reduce card or cash payment by amount

        # Check if this payback is via card or cash
        via_card = self.payment_method == DebtPaybackMethod.CARD
        via_cash = self.payment_method == DebtPaybackMethod.CASH

        # if Debt Payback is for expense
        if self.type == FarmDebtPaybackType.OUTGOINGS:
            if via_card:
                self.expense.card_payment -= self.amount
            elif via_cash:
                self.expense.cash_payment -= self.amount
            self.expense.debt_payment += self.amount
            self.expense.save()

        # if Debt Payback is for sales
        elif self.type == FarmDebtPaybackType.INCOME:
            if via_card:
                self.sales_report.card_payment -= self.amount
            elif via_cash:
                self.sales_report.cash_payment -= self.amount
            self.sales_report.debt_payment += self.amount
            self.sales_report.save()
