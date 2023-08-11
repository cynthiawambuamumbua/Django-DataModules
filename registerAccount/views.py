from django.shortcuts import render
from.forms import RegisterAccountUploadForm
# from inventory.models import Product
# from django.shortcuts import redirect

# Create your views here.
def registerAccount_upload_view(request):
    form =RegisterAccountUploadForm()
    return render(request,"registerAccount/registerAccount_upload.html",{"form":form})