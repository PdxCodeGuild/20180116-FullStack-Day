from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    fulfilled_date = models.DateTimeField(null=True, blank=True)
    #total = models.FloatField()

    def __str__(self):
        return str(self.created_date)

    def total(self):
        r = 0.0
        for order_item in self.items.all():
            r += order_item.item.unit_price*order_item.quantity
        return r


class Item(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order)


