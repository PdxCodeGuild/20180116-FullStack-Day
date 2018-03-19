from django.db import models


class Coupon(models.Model):
    name = models.CharField(max_length=100)
    percent_off = models.FloatField()

    def __str__(self):
        return self.name


class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name

    def pretty_unit_price(self):
        return '{0:.2f}'.format(self.unit_price)

class GroceryList(models.Model):
    name = models.CharField(max_length=100)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_total_sans_coupon(self):
        total = 0.0
        for grocery_list_item in self.grocerylistitem_set.all():
            total += grocery_list_item.quantity * grocery_list_item.grocery_item.unit_price
        return '{0:.2f}'.format(total)

    def get_total(self):
        total = 0.0
        for grocery_list_item in self.grocerylistitem_set.all():
            total += grocery_list_item.quantity * grocery_list_item.grocery_item.unit_price

        # coupon_percent = 0 if self.coupons.count() == 0 else self.coupons.all()[0].percent_off
        coupon_percent = 0 if self.coupon is None else self.coupon.percent_off

        return '{0:.2f}'.format(total*(1.0-coupon_percent/100.0)) + ' (' + str(coupon_percent) + '% off)'



class GroceryListItem(models.Model):
    grocery_item = models.ForeignKey(GroceryItem, on_delete=models.CASCADE)
    grocery_list = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.grocery_list.name + ' - ' + self.grocery_item.name




