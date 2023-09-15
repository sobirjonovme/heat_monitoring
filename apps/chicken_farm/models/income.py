from django.core.exceptions import ValidationError
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
        # update productivity
        if previous_report:
            # update remaining chickens
            self.remaining_chickens = previous_report.remaining_chickens - self.dead_chickens
            # update total remaining eggs
            self.total_remaining_eggs = (
                previous_report.total_remaining_eggs + self.laid_eggs - self.broken_eggs - self.sold_egg_boxes * 30
            )
        else:
            # if there is no previous report
            # then update remaining chickens and total remaining eggs according to initial farm resource count
            from apps.chicken_farm.models.common import FarmResource

            farm_resource = FarmResource.get_solo()
            self.remaining_chickens = farm_resource.initial_chickens_count - self.dead_chickens
            self.total_remaining_eggs = (
                farm_resource.initial_eggs_count + self.laid_eggs - self.broken_eggs - self.sold_egg_boxes * 30
            )
        productivity = int(self.laid_eggs) / int(self.remaining_chickens) * 100
        # round productivity to 1 decimal places
        self.productivity = round(productivity, 1)
        self.save()
        return self

    def clean(self):
        # check if there is not a daily report with this date
        if FarmDailyReport.objects.filter(date=self.date, via_sales_report=False).exclude(id=self.id).exists():
            raise ValidationError(code="invalid", message={"date": _("A daily report with this date already exists.")})

    def save(self, *args, **kwargs):
        self.full_clean()
        # delete if there is a daily report with the same date created via sales report
        FarmDailyReport.objects.filter(date=self.date, via_sales_report=True).delete()
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        # update next report according to this report deletion
        next_report = FarmDailyReport.objects.filter(date__gt=self.date).order_by("date").first()
        res = super().delete(using=using, keep_parents=keep_parents)

        if next_report:
            from apps.chicken_farm.utils import bulk_update_daily_reports

            bulk_update_daily_reports(next_report)
        else:
            # if there is no next report, then update FarmResource
            from apps.chicken_farm.models.common import FarmResource

            FarmResource.update_according_to_last_report()

        return res


class FarmSalesReport(TimeStampedModel):
    sold_egg_boxes = models.PositiveIntegerField(  # in boxes, not single eggs
        verbose_name=_("sold eggs"), help_text=_("sold eggs in boxes")
    )
    price_per_box = models.PositiveIntegerField(verbose_name=_("price per box"))
    comment = models.TextField(verbose_name=_("comment"), null=True, blank=True)
    card_payment = models.DecimalField(verbose_name=_("Card money"), max_digits=12, decimal_places=2, default=0)
    cash_payment = models.DecimalField(verbose_name=_("Cash money"), max_digits=12, decimal_places=2, default=0)
    debt_payment = models.DecimalField(verbose_name=_("Debt money"), max_digits=12, decimal_places=2, default=0)
    phone_number = models.CharField(verbose_name=_("phone number"), max_length=20, null=True, blank=True)
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
        return int(self.sold_egg_boxes) * 30

    def get_local_sold_at(self):
        # convert sold_at to local timezone
        return timezone.localtime(self.sold_at)

    def delete(self, using=None, keep_parents=False):
        # update next report according to this report deletion
        res = super().delete(using=using, keep_parents=keep_parents)

        # Update FarmDailyReport and FarmResource after deleting this sales report
        self.apply_to_related_daily_report()

        return res

    def apply_to_related_daily_report(self):
        # get sold date in local timezone
        sold_date = self.get_local_sold_at().date()

        start_daily_report = FarmDailyReport.objects.filter(date=sold_date).first()
        if not start_daily_report:
            start_daily_report = FarmDailyReport.objects.create(date=sold_date, via_sales_report=True)

        from apps.chicken_farm.utils import bulk_update_daily_reports

        bulk_update_daily_reports(start_daily_report)

        return start_daily_report
