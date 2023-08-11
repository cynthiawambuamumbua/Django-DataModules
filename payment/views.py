from django.shortcuts import render
from.forms import PaymentUploadForm
from payment.models import Payment
# from django.shortcuts import redirect

# Create your views here.
def payment_upload_view(request):
    form =PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})

def payment_list(request):
    payment= Payment.objects.all()
    return render(request,"payment/payment_list.html",{"payment":payment})