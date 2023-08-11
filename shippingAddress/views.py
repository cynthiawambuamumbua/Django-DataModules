from django.shortcuts import render
from.forms import ShippingAddressUploadForm
# from inventory.models import Product
# from django.shortcuts import redirect

# Create your views here.
def shippingAddress_upload_view(request):
    form =ShippingAddressUploadForm()
    return render(request,"shippingAddress/shippingAddress_upload.html",{"form":form})