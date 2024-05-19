from django.db import models
from products.models import Item

class Order(models.Model):
    order_status = models.CharField(max_length=20, default='Not Delivered')

    def __str__(self):
        return f"Order #{self.pk}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.name} for Order #{self.order.pk}"
