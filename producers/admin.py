from django.contrib import admin
from .models import Producer


class ProducerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'highlight',
    )


admin.site.register(Producer, ProducerAdmin)
