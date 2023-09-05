from django.shortcuts import render
from.forms import CustomerUploadForm
from customer.models import Customer
from django.shortcuts import redirect

# Create your views here.
def customer_upload_view(request):
    form =CustomerUploadForm()
    return render(request,"customer/customer_upload.html",{"form":form})

def customer_list(request):
    customer= Customer.objects.all()
    return render(request,"customer/customer_list.html",{"customer":customer})

def customer_detail_view(request,id):
    customer=Customer.objects.all()
    return render(request,"customer/customer_details.html",{"customer":customer})

def edit_customer_view(request,id):
    customer=Customer.objects.get(id=id)
    if request.method=="POST":
        form=CustomerUploadForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_detail_view',id=customer)
        else:
            form=CustomerUploadForm(instance=customer)
            return render(request,'edit/edit_customer.html',{'form':form})
        