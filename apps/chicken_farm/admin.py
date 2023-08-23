from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.chicken_farm.models import (FarmDailyReport, FarmDebtPayback,
                                      FarmExpense, FarmExpenseType,
                                      FarmResource, FarmSalesReport)
from apps.chicken_farm.utils import bulk_update_daily_reports


# Register your models here.
@admin.register(FarmResource)
class FarmResourceAdmin(SingletonModelAdmin):
    pass


@admin.register(FarmDailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "laid_eggs",
        "broken_eggs",
        "dead_chickens",
        "total_remaining_eggs",
        "remaining_chickens",
    )
    list_display_links = ("id", "date")
    search_fields = ("id", "date")
    readonly_fields = ("reported_by", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        # find most recent daily report
        most_recent_date = obj.date
        if obj.id:
            most_recent_date = min(FarmDailyReport.objects.get(id=obj.id).date, most_recent_date)
        else:
            # delete if there is a daily report with the same date created via sales report
            FarmDailyReport.objects.filter(date=obj.date, via_sales_report=True).delete()
        obj.save()

        # update daily report posted before this daily report and FarmResource
        most_recent_report = FarmDailyReport.objects.filter(date__lte=most_recent_date).order_by("-date").first()
        if not most_recent_report:
            most_recent_report = FarmDailyReport.objects.filter(date__gte=most_recent_date).order_by("date").first()
        bulk_update_daily_reports(most_recent_report)


@admin.register(FarmSalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ("id", "sold_at", "sold_egg_boxes", "price_per_box", "total_payment")
    list_display_links = ("id", "sold_at")
    search_fields = ("id", "sold_at")
    readonly_fields = ("reported_by", "created_at", "updated_at")

    def save_model(self, request, obj, form, change):
        # find most recent daily report
        most_recent_date = obj.get_local_sold_at().date()
        if obj.id:
            most_recent_date = min(FarmSalesReport.objects.get(id=obj.id).get_local_sold_at().date(), most_recent_date)
        obj.save()
        # update daily report posted before this sales report and FarmResource
        related_daily_report = FarmDailyReport.objects.filter(date=most_recent_date).first()
        if not related_daily_report:
            related_daily_report = FarmDailyReport.objects.create(date=most_recent_date, via_sales_report=True)
        bulk_update_daily_reports(related_daily_report)


@admin.register(FarmDebtPayback)
class IncomeDebtPaybackAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "payment_method", "type", "paid_at")
    list_display_links = ("id", "amount")
    search_fields = ("id", "paid_at", "amount")
    list_filter = (
        "payment_method",
        "type",
    )
    readonly_fields = ("reported_by", "created_at", "updated_at")


@admin.register(FarmExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = (
        "id",
        "name",
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(FarmExpense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "card_payment", "cash_payment", "debt_payment", "date")
    list_display_links = ("id", "type", "date")
    search_fields = ("id", "type__name")
    readonly_fields = ("reported_by", "created_at", "updated_at")
