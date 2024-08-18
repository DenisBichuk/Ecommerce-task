from django.contrib import admin

from . import inlines, mixins, models


@admin.register(models.Category)
class CategoryAdmin(mixins.AdminPageLimit, admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = (
        'title',
    )


@admin.register(models.Equipment)
class EquipmentAdmin(mixins.AdminPageLimit, admin.ModelAdmin):
    list_display = (
        'title',
        'quantity',
        'stock',
        'category',
        'user',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'category__title',
        'user__email',
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'title',
        'category__title',
        'stock__title',
        'stock__address',
    )
    date_hierarchy = 'created_at'


@admin.register(models.Stock)
class StockAdmin(mixins.AdminPageLimit, admin.ModelAdmin):
    list_display = (
        'title',
        'address',
    )
    search_fields = (
        'title',
        'address',
    )
    inlines = (
        inlines.EquipmentInline,
    )
