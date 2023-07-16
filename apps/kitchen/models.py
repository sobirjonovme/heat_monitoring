from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel

from .choices import OrderStatus


class ProductUnit(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=127)
    short_name = models.CharField(verbose_name=_("Short name"), max_length=15)
    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)

    def __str__(self):
        return self.short_name


class Product(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    unit = models.ForeignKey(ProductUnit, verbose_name=_("Unit"), on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(verbose_name=_("Order"), default=0)
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    status = models.CharField(
        verbose_name=_("Status"), max_length=15, choices=OrderStatus.choices, default=OrderStatus.NEW
    )
    ordered_by = models.ForeignKey(
        to="users.User",
        verbose_name=_("Ordered by"),
        related_name="created_orders",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    delivered_by = models.ForeignKey(
        to="users.User",
        verbose_name=_("Delivered by"),
        related_name="delivered_orders",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Order #{self.id} - {self.status}"


class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
        to="kitchen.Order", verbose_name=_("Order"), related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to="kitchen.Product", verbose_name=_("Product"), related_name="orders", on_delete=models.PROTECT
    )
    needed_quantity = models.DecimalField(verbose_name=_("Unit quantity"), max_digits=10, decimal_places=2)
    delivered_quantity = models.DecimalField(
        verbose_name=_("Delivered quantity"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2, null=True, blank=True)
    is_checked = models.BooleanField(verbose_name=_("Is checked"), default=False)
    checked_by = models.ForeignKey(
        to="users.User",
        verbose_name=_("Checked by"),
        related_name="checked_orders",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.name}"
