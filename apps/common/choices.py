from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.TextChoices):
    CARD = "CARD", _("Card")
    CASH = "CASH", _("Cash")
    DEBT = "DEBT", _("Debt")


class DebtPaybackMethod(models.TextChoices):
    CARD = "CARD", _("Card")
    CASH = "CASH", _("Cash")
