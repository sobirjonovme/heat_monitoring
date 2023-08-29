from django.db import models
from django.utils.translation import gettext_lazy as _


class FarmDebtPaybackType(models.TextChoices):
    INCOME = "INCOME", _("Income")
    OUTGOINGS = "OUTGOINGS", _("Outgoings")


class FarmExpenseCategory(models.TextChoices):
    FODDER = "FODDER", _("Fodder")
    OTHER = "OTHER", _("Other")
