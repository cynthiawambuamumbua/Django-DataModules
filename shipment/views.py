from django.shortcuts import render
from.forms import ShipmentUploadForm
# from inventory.models import Product
# from django.shortcuts import redirect

# Create your views here.
def shipment_upload_view(request):
    form =ShipmentUploadForm()
    return render(request,"shipment/shipment_upload.html",{"form":form})