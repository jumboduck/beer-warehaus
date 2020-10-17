from django.contrib import admin
from .models import Product, Producer, Style, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'producer',
        'name',
        'volume',
    )

    ordering = ('sku',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Producer)
admin.site.register(Style)
