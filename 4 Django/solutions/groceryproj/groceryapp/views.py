from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Coupon, GroceryItem, GroceryList, GroceryListItem


def index(request):
    grocery_lists = GroceryList.objects.order_by('name')
    return render(request, 'groceryapp/index.html', {'grocery_lists': grocery_lists})


def detail(request, grocery_list_id):
    # grocery_list = GroceryList.objects.get(pk=grocery_list_id)
    grocery_list = get_object_or_404(GroceryList, pk=grocery_list_id)
    return render(request, 'groceryapp/detail.html', {'grocery_list': grocery_list})
