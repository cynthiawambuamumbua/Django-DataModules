from django.shortcuts import render
from.forms import CustomerUploadForm
from customer.models import Customer
# from django.shortcuts import redirect

# Create your views here.
def customer_upload_view(request):
    form =CustomerUploadForm()
    return render(request,"customer/customer_upload.html",{"form":form})

def customer_list(request):
    customer= Customer.objects.all()
    return render(request,"customer/customer_list.html",{"customer":customer})