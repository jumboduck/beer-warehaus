from django.contrib import admin
from .models import Product, Style, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'producer',
        'sku',
        'volume',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
    )

    ordering = ('friendly_name',)


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'category',
    )

    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Product, ProductAdmin)
