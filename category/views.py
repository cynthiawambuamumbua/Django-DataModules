from django.shortcuts import render
from.forms import CategoryUploadForm
from category.models import Category
# # from django.shortcuts import redirect

# Create your views here.
def category_upload_view(request):
    form =CategoryUploadForm()
    return render(request,"category/category_upload.html",{"form":form})

def category_list(request):
    category= Category.objects.all()
    return render(request,"category/category_list.html",{"category":category})