from django.shortcuts import render
from.forms import ShippingAddressUploadForm
from shippingAddress.models import ShippingAddress
from django.shortcuts import redirect

# Create your views here.
def shippingAddress_upload_view(request):
    form =ShippingAddressUploadForm()
    return render(request,"shippingAddress/shippingAddress_upload.html",{"form":form})

def shippingAddress_list(request):
    shippingAddress= ShippingAddress.objects.all()
    return render(request,"shippingAddress/shippingAddress_list.html",{"shippingAddress":shippingAddress})

def shippingAddress_detail_view(request,id):
    shippingAddress= ShippingAddress.objects.all()
    return render(request,"shoipingAddress/shippingAddress_detail.html",{"shippingAddress":shippingAddress})

def edit_shippingAddress_view(request,id):
    shippingAddress=ShippingAddress.objects.get(id=id)
    if request.method=="POST":
        form=ShippingAddressUploadForm(request.POST,instance=shippingAddress)
        if form.is_valid():
            form.save()
            return redirect('shippingAddress_detail_view',id=shippingAddress)
        else:
            form=ShippingAddressUploadForm(instance=shippingAddress)
            return render(request,'shippingAddress/edit_shippingAddress.html',{'form':form})