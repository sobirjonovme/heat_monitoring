from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel

from .managers import DailyReportManager


# Create your models here.
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
    via_sales_report = models.BooleanField(verbose_name=_("via sales report"), default=False)

    objects = DailyReportManager()

    class Meta:
        verbose_name = _("daily report")
        verbose_name_plural = _("daily reports")

    def __str__(self):
        return f"#{self.id} - {self.date}"

    @property
    def sold_egg_boxes(self):
        sales_reports = FarmSalesReport.objects.filter(sold_at__date=self.date).distinct()
        if sales_reports:
            return sales_reports.aggregate(models.Sum("sold_egg_boxes"))["sold_egg_boxes__sum"]
        return 0

    def update_according_to_previous(self, previous_report=None):
        if not previous_report:
            # get previous daily report
            previous_report = FarmDailyReport.objects.filter(date__lt=self.date).order_by("-date").first()
        if previous_report:
            # update remaining chickens
            self.remaining_chickens = previous_report.remaining_chickens - self.dead_chickens
            # update total remaining eggs
            self.total_remaining_eggs = (
                previous_report.total_remaining_eggs + self.laid_eggs - self.broken_eggs - self.sold_egg_boxes * 30
            )
        elif FarmDailyReport.objects.filter(date__gt=self.date).exists():
            # if there is no previous report, but there is a report after this one
            # then update remaining chickens and total remaining eggs according to the next report
            next_report = FarmDailyReport.objects.filter(date__gt=self.date).order_by("date").first()
            self.remaining_chickens = next_report.remaining_chickens + next_report.dead_chickens - self.dead_chickens
            self.total_remaining_eggs = (
                next_report.total_remaining_eggs
                - next_report.laid_eggs
                + next_report.broken_eggs
                + self.laid_eggs
                - self.sold_egg_boxes * 30
                - self.broken_eggs
            )
        else:
            # if there is no previous report and no report after this one
            # then update remaining chickens and total remaining eggs according to FarmResource
            from apps.chicken_farm.models.common import FarmResource

            farm_resource = FarmResource.get_solo()
            self.remaining_chickens = farm_resource.remaining_chickens - self.dead_chickens
            self.total_remaining_eggs = (
                farm_resource.total_remaining_eggs + self.laid_eggs - self.broken_eggs - self.sold_egg_boxes * 30
            )
        # update productivity
        productivity = int(self.laid_eggs) / int(self.remaining_chickens) * 100
        # round productivity to 1 decimal places
        self.productivity = round(productivity, 1)
        self.save()
        return self


class FarmSalesReport(TimeStampedModel):
    sold_egg_boxes = models.PositiveIntegerField(  # in boxes, not single eggs
        verbose_name=_("sold eggs"), default=0, help_text=_("sold eggs in boxes")
    )
    price_per_box = models.PositiveIntegerField(verbose_name=_("price per box"), default=0)
    comment = models.TextField(verbose_name=_("comment"), null=True, blank=True)
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

    def __str__(self):
        return f"#{self.id} - {self.sold_at}"

    @property
    def total_payment(self):
        return self.price_per_box * self.sold_egg_boxes

    @property
    def sold_eggs_count(self):
        return int(self.sold_eggs) * 30
