from django.contrib import admin

from apps.kitchen.models import Order, OrderItem, Product, ProductUnit


@admin.register(ProductUnit)
class ProductUnitAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "short_name", "order")
    list_display_links = ("id", "name", "short_name")
    search_fields = ("id", "name", "short_name")
    ordering = ("order", "name")
    list_editable = ("order",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "unit", "order", "is_active")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    ordering = ("order", "name")
    list_editable = ("order", "is_active")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status",
        "ordered_by",
        "delivered_by",
    )
    list_display_links = ("id",)
    search_fields = (
        "id",
        "status",
        "ordered_by__first_name",
        "ordered_by__last_name",
        "delivered_by__first_name",
        "delivered_by__last_name",
    )
    list_filter = ("status",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "needed_quantity", "delivered_quantity", "price", "is_checked")
    list_display_links = ("id",)
    search_fields = ("id", "order__id", "product__name")
    list_filter = ("product", "order")
