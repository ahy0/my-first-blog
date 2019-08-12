from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'shop/item_list.html', {
        'item_list': items,
    })