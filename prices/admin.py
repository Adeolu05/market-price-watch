from django.contrib import admin

from .models import Item, Market, PriceReport

admin.site.site_header = "Market Price Watch Admin"
admin.site.site_title = "Price Watch"
admin.site.index_title = "Manage markets, items and prices"


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "state"]
    list_filter = ["state"]
    search_fields = ["name", "city"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "unit", "category"]
    list_filter = ["category"]
    search_fields = ["name"]


@admin.register(PriceReport)
class PriceReportAdmin(admin.ModelAdmin):
    list_display = ["item", "market", "price", "reported_at"]
    list_filter = ["market", "item__category", "reported_at"]
    search_fields = ["item__name", "market__name"]
    date_hierarchy = "reported_at"