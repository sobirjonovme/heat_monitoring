from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.chicken_farm.models import (FarmDailyReport, FarmResource,
                                      FarmSalesReport)


# Register your models here.
@admin.register(FarmResource)
class FarmResourceAdmin(SingletonModelAdmin):
    pass


@admin.register(FarmDailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "laid_eggs", "broken_eggs", "dead_chickens")
    list_display_links = ("id", "date")
    search_fields = ("id", "date")
    readonly_fields = ("reported_by", "created_at", "updated_at")


@admin.register(FarmSalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ("id", "sold_at", "sold_eggs", "price_per_box", "total_payment")
    list_display_links = ("id", "sold_at")
    search_fields = ("id", "sold_at")
    readonly_fields = ("reported_by", "created_at", "updated_at")
