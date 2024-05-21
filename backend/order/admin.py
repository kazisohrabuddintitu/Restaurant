from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    fields = ('item', 'quantity', 'special_request')  # Display these fields in the inline
    readonly_fields = ('item',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'table_number', 'order_status')
    list_filter = ('order_status',)
    inlines = [OrderItemInline]

    def get_ordering(self, request):
        return ['order_status']  # Ensures not delivered orders are on top

admin.site.register(Order, OrderAdmin)
