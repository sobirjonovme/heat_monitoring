from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.chicken_farm.models import DailyReport, FarmResource


# Register your models here.
@admin.register(FarmResource)
class FarmResourceAdmin(SingletonModelAdmin):
    pass


@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "laid_eggs", "broken_eggs", "sold_eggs", "dead_chickens")
    list_display_links = ("id", "date")
    search_fields = ("id", "date")
    readonly_fields = ("reported_by", "created_at", "updated_at")
