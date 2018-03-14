from django.contrib import admin
from .models import GroceryItem, Coupon, GroceryList, GroceryListItem

admin.site.register(GroceryItem)
admin.site.register(Coupon)
admin.site.register(GroceryList)
admin.site.register(GroceryListItem)

