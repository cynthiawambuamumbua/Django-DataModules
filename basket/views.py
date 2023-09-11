from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Basket, Order, Payment, Shipment,Product
from .forms import PaymentForm, ShipmentForm

def remove_product(request, basket_id, product_id):
    basket = get_object_or_404(Basket, id=basket_id)
    product = get_object_or_404(Product, id=product_id)
    basket.products.remove(product)
    
    return redirect('basket:detail', basket_id=basket_id)

def checkout(request, basket_id):
    basket = get_object_or_404(Basket, id=basket_id)
    order = Order.objects.create(basket=basket)    
    return redirect('order:detail', order_id=order.id)

def payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.save()
            return redirect('order:detail', order_id=order.id)
    else:
        form = PaymentForm()
    
    return render(request, 'basket/payment.html', {'form': form})

def shipment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.order = order
            shipment.save()
            return redirect('order:detail', order_id=order.id)
    else:
        form = ShipmentForm()
    return render(request, 'basket/shipment.html', {'form': form})