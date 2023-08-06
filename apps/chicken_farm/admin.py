from django.contrib import admin
from solo.admin import SingletonModelAdmin

from apps.chicken_farm.models import (FarmDailyReport, FarmDebtPayback,
                                      FarmExpense, FarmExpenseType,
                                      FarmResource, FarmSalesReport)


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
