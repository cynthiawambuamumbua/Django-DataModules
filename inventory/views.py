from django.shortcuts import render
from.forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import redirect

# Create your views here.
def product_upload_view(request):
    form =ProductUploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})

def products_list(request):
    products= Product.objects.all()
    return render(request,"inventory/products_list.html",{"products":products})

def product_detail_view(request,id):
    products=Product.objects.all()
    return render(request,"inventory/product_details.html",{"products":products})

def edit_product_view(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        form=ProductUploadForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail_view',id=product)
        else:
            form=ProductUploadForm(instance=product)
            return render(request,'edit/edit_product.html',{'form':form})

