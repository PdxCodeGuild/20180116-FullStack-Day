from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Coupon, GroceryItem, GroceryList, GroceryListItem


def index(request):
    grocery_lists = GroceryList.objects.order_by('name')
    return render(request, 'groceryapp/index.html', {'grocery_lists': grocery_lists})


def detail(request, grocery_list_id):
    # grocery_list = GroceryList.objects.get(pk=grocery_list_id)
    grocery_list = get_object_or_404(GroceryList, pk=grocery_list_id)
    grocery_items = GroceryItem.objects.order_by('name')
    coupons = Coupon.objects.order_by('name')
    context = {'grocery_list': grocery_list, 'grocery_items': grocery_items, 'coupons':coupons}
    return render(request, 'groceryapp/detail.html', context)



def additem(request, grocery_list_id):
    grocery_list = GroceryList.objects.get(pk=grocery_list_id)
    grocery_item_id = request.POST['grocery_item_id']
    quantity = request.POST['quantity']
    grocery_item = GroceryItem.objects.get(pk=grocery_item_id)

    grocery_list_item = grocery_list.grocerylistitem_set.filter(grocery_item_id=grocery_item_id).first()
    if grocery_list_item is None:
        grocery_list_item = GroceryListItem(grocery_list=grocery_list, grocery_item=grocery_item, quantity=quantity)
        grocery_list_item.save()
    else:
        grocery_list_item.quantity += int(quantity)
        grocery_list_item.save()

    return HttpResponseRedirect(reverse('groceryapp:detail', kwargs={'grocery_list_id':grocery_list_id}))



def applycoupon(request, grocery_list_id):
    grocery_list = GroceryList.objects.get(pk=grocery_list_id)
    coupon_id = request.POST['coupon_id']
    if coupon_id == 'null':
        grocery_list.coupon = None
    else:
        grocery_list.coupon_id = coupon_id
    grocery_list.save()

    return HttpResponseRedirect(reverse('groceryapp:detail', kwargs={'grocery_list_id':grocery_list_id}))




def handler404(request):
    return HttpResponseRedirect('https://http.cat/404')


def handler500(request):
    return HttpResponseRedirect('https://http.cat/500')

