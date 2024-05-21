from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_top_ordered')

    def is_top_ordered(self, obj):
        return obj.top_ordered > 0
    is_top_ordered.boolean = True
    is_top_ordered.short_description = 'Top Ordered'

admin.site.register(Item, ItemAdmin)