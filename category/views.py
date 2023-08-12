from django.shortcuts import render
from.forms import CategoryUploadForm
from category.models import Category
from django.shortcuts import redirect

# Create your views here.
def category_upload_view(request):
    form =CategoryUploadForm()
    return render(request,"category/category_upload.html",{"form":form})

def category_list(request):
    category= Category.objects.all()
    return render(request,"category/category_list.html",{"category":category})

def category_detail_view(request,id):
    category=Category.objects.all()
    return render(request,"category/category_detail.html",{"category":category})

def edit_category_view(request,id):
    category=Category.objects.get(id=id)
    if request.method=="POST":
        form=CategoryUploadForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail_view',id=category)
        else:
            form=CategoryUploadForm(instance=category)
            return render(request,'edit/edit_category.html',{'form':form})
