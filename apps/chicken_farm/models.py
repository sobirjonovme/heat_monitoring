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


class DailyReport(TimeStampedModel):
    laid_eggs = models.PositiveIntegerField(verbose_name=_("laid eggs"), default=0)
    broken_eggs = models.PositiveIntegerField(verbose_name=_("broken eggs"), default=0)
    sold_eggs = models.PositiveIntegerField(verbose_name=_("sold eggs"), default=0)
    dead_chickens = models.PositiveIntegerField(verbose_name=_("dead chickens"), default=0)
    total_remaining_eggs = models.PositiveIntegerField(verbose_name=_("total remaining eggs"), null=True, blank=True)
    productivity = models.FloatField(verbose_name=_("productivity"), null=True, blank=True)
    date = models.DateField(verbose_name=_("date"), default=timezone.now)
    reported_by = models.ForeignKey(
        verbose_name=_("Reported by"), to="users.User", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = _("daily report")
        verbose_name_plural = _("daily reports")

    def __str__(self):
        return f"{self.id} - {self.date}"
