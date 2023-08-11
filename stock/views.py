from django.shortcuts import render
from.forms import StockUploadForm
# from inventory.models import Product
# from django.shortcuts import redirect

# Create your views here.
def stock_upload_view(request):
    form =StockUploadForm()
    return render(request,"stock/stock_upload.html",{"form":form})