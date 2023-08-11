from django.shortcuts import render
from.forms import ShipmentUploadForm
from shipment.models import Shipment
# from django.shortcuts import redirect

# Create your views here.
def shipment_upload_view(request):
    form =ShipmentUploadForm()
    return render(request,"shipment/shipment_upload.html",{"form":form})

def shipment_list(request):
    shipment= Shipment.objects.all()
    return render(request,"shipment/shipment_list.html",{"shipment":shipment})