from django.db import models
# from django.contrib.auth.models import AbstractUser, User
# Create your models here.


# class UserProfile(AbstractUser):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#

class Order(models.Model):
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    fulfilled_date = models.DateTimeField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.created_date)

    def get_total(self):
        t = 0
        for order_item in self.items.all():
            t += order_item.item.unit_price * order_item.quantity
        self.total = t
        return t


class Item(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  #items_set.all()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order)
