from django.contrib import admin
from .models import Algorithm

# Register your models here.

# admin.site.register(Algorithm)


@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'item_count', 'sort_percentage', 'time')
    list_filter = ('type', 'item_count', 'sort_percentage')
