from django.shortcuts import render
from.forms import ShipmentUploadForm
from shipment.models import Shipment
from django.shortcuts import redirect

# Create your views here.
def shipment_upload_view(request):
    form =ShipmentUploadForm()
    return render(request,"shipment/shipment_upload.html",{"form":form})

def shipment_list(request):
    shipment= Shipment.objects.all()
    return render(request,"shipment/shipment_list.html",{"shipment":shipment})

def shipment_detail_view(request,id):
    shipment= Shipment.objects.all()
    return render(request,"shipment/shipment_detail.html",{"shipment":shipment})

def edit_shipment_view(request,id):
    shipment=Shipment.objects.get(id=id)
    if request.method=="POST":
        form=ShipmentUploadForm(request.POST,instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('shipment_detail_view',id=shipment)
        else:
            form=ShipmentUploadForm(instance=shipment)
            return render(request,'shipment/edit_shipment.html',{'form':form})