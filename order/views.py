from django.shortcuts import render
from.forms import OrderUploadForm
from order.models import Order
from django.shortcuts import redirect

# Create your views here.
def order_upload_view(request):
    form =OrderUploadForm()
    return render(request,"order/order_upload.html",{"form":form})

def order_list(request):
    order= Order.objects.all()
    return render(request,"order/order_list.html",{"order":order})

def order_detail_view(request):
    order=Order.objects.all()
    return render(request,"order/order_details.html",{"order":order})

def edit_order_view(request,id):
    order=Order.objects.get(id=id)
    if request.method=="POST":
        form=OrderUploadForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail_view',id=order)
        else:
            form=OrderUploadForm(instance=order)
            return render(request,'edit/edit_order.html',{'form':form})