from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from apps.chicken_farm.choices import FarmExpenseCategory
from apps.common.models import TimeStampedModel


class FarmExpenseType(TimeStampedModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    category = models.CharField(verbose_name=_("category"), max_length=15, choices=FarmExpenseCategory.choices)
    amount = models.FloatField(verbose_name=_("amount"), default=0)

    class Meta:
        verbose_name = _("expense type")
        verbose_name_plural = _("expense types")

    def __str__(self):
        return self.name


class FarmExpense(TimeStampedModel):
    type = models.ForeignKey(
        verbose_name=_("type"), to="chicken_farm.FarmExpenseType", on_delete=models.CASCADE, related_name="expenses"
    )
    item_amount = models.FloatField(verbose_name=_("item amount"))
    item_unit = models.CharField(verbose_name=_("item unit"), max_length=127)
    card_payment = models.DecimalField(verbose_name=_("Card money"), max_digits=10, decimal_places=2, default=0)
    cash_payment = models.DecimalField(verbose_name=_("Cash money"), max_digits=10, decimal_places=2, default=0)
    debt_payment = models.DecimalField(verbose_name=_("Debt money"), max_digits=10, decimal_places=2, default=0)
    comment = models.TextField(verbose_name=_("comment"), null=True, blank=True)
    image = ImageField(verbose_name=_("image"), upload_to="expenses/%Y/%m/%d/", null=True, blank=True)
    date = models.DateField(verbose_name=_("date"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("expense")
        verbose_name_plural = _("expenses")

    def __str__(self):
        return f"#{self.id} - {self.type}"

    @property
    def total_payment(self):
        return self.card_payment + self.cash_payment + self.debt_payment

    def reduce_expense_type_amount(self):
        self.type.amount -= self.item_amount
        self.type.save()

    def increase_expense_type_amount(self):
        self.type.amount += self.item_amount
        self.type.save()


class FarmFodderIngredientUsage(TimeStampedModel):
    ingredient = models.ForeignKey(
        verbose_name=_("ingredient"), to="chicken_farm.FarmExpenseType", on_delete=models.CASCADE
    )
    amount = models.FloatField(verbose_name=_("amount"))
    remaining_amount = models.FloatField(verbose_name=_("remaining amount"), null=True, blank=True)  # not used for now
    date = models.DateField(verbose_name=_("date"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("fodder ingredient usage")
        verbose_name_plural = _("fodder ingredients usage")

    def __str__(self):
        return f"#{self.id} - {self.ingredient.name}"

    def reduce_ingredient_amount(self):
        self.ingredient.amount -= self.amount
        self.ingredient.save()

    def increase_ingredient_amount(self):
        self.ingredient.amount += self.amount
        self.ingredient.save()
