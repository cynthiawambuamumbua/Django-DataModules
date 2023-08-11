from django.shortcuts import render
from.forms import RegisterAccountUploadForm
from registerAccount.models import RegisterAccount
# from django.shortcuts import redirect

# Create your views here.
def registerAccount_upload_view(request):
    form =RegisterAccountUploadForm()
    return render(request,"registerAccount/registerAccount_upload.html",{"form":form})

def registerAccount_list(request):
    registerAccount= RegisterAccount.objects.all()
    return render(request,"registerAccount/registerAccount_list.html",{"registerAccount":registerAccount})