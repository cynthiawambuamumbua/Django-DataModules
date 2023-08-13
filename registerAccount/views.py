from django.shortcuts import render
from.forms import RegisterAccountUploadForm
from registerAccount.models import RegisterAccount
from django.shortcuts import redirect

# Create your views here.
def registerAccount_upload_view(request):
    form =RegisterAccountUploadForm()
    return render(request,"registerAccount/registerAccount_upload.html",{"form":form})

def registerAccount_list(request):
    registerAccount= RegisterAccount.objects.all()
    return render(request,"registerAccount/registerAccount_list.html",{"registerAccount":registerAccount})

def registerAccount_detail_view(request,id):
    registerAccount=RegisterAccount.objects.all()
    return render(request,"registerAccount/registerAccount_details.html",{"registerAccount":registerAccount})

def edit_registerAccount_view(request,id):
    registerAccount=RegisterAccount.objects.get(id=id)
    if request.method=="POST":
        form=RegisterAccountUploadForm(request.POST,instance=registerAccount)
        if form.is_valid():
            form.save()
            return redirect('registerAccount_detail_view',id=registerAccount)
        else:
            form=RegisterAccountUploadForm(instance=registerAccount)
            return render(request,'registerAccount/edit_registerAccount.html',{'form':form})