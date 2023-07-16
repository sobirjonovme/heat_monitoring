from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    NEW = "new", _("New")
    DELIVERED = "delivered", _("Delivered")
    CHECKED = "checked", _("Checked")
