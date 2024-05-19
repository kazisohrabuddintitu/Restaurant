from django.db import models
from products.models import Item

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    special_request = models.TextField(blank=True)
    order_status = models.CharField(max_length=20, default='Not Delivered')

    def __str__(self):
        return f"Order #{self.pk}"
