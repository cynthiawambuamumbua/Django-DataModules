from django.shortcuts import render
from.forms import OrderUploadForm
from order.models import Order
# from django.shortcuts import redirect

# Create your views here.
def order_upload_view(request):
    form =OrderUploadForm()
    return render(request,"order/order_upload.html",{"form":form})

def order_list(request):
    order= Order.objects.all()
    return render(request,"order/order_list.html",{"orders":order})