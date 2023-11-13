from django.shortcuts import render, get_object_or_404, redirect
from .models import Basket
from inventory.models import Product

def basket_detail(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)
    total = basket.get_total()

    context = {
        'basket': basket,
        'total': total,
    }

    return render(request, 'basket/basket_detail.html', context)
