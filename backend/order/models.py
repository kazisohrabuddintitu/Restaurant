from django.db import models
from products.models import Item

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('not_delivered', 'Not Delivered'),
        ('delivered', 'Delivered'),
    ]

    customer_name = models.CharField(max_length=100)
    table_number = models.CharField(max_length=10, blank=True, null=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='not_delivered')

    def __str__(self):
        return f'Order {self.id} by {self.customer_name}'

    class Meta:
        ordering = ['order_status']  # Not delivered orders on top


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    special_request = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.quantity} x {self.item.name} for {self.order}'
