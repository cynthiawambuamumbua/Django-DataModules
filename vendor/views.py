from django.shortcuts import render
from.forms import VendorUploadForm
# from inventory.models import Product
# from django.shortcuts import redirect

# Create your views here.
def vendor_upload_view(request):
    form =VendorUploadForm()
    return render(request,"vendor/vendor_upload.html",{"form":form})