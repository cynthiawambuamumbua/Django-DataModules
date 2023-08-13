from django.shortcuts import render
from.forms import PaymentUploadForm
from payment.models import Payment
from django.shortcuts import redirect

# Create your views here.
def payment_upload_view(request):
    form =PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})

def payment_list(request):
    payment= Payment.objects.all()
    return render(request,"payment/payment_list.html",{"payment":payment})

def payment_detail_view(request,id):
    payment=Payment.objects.all()
    return render(request,"payment/payment_details.html",{"payment":payment})

def edit_payment_view(request,id):
    payment=Payment.objects.get(id=id)
    if request.method=="POST":
        form=PaymentUploadForm(request.POST,instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_detail_view',id=payment)
        else:
            form=PaymentUploadForm(instance=payment)
            return render(request,'payment/edit_payment.html',{'form':form})