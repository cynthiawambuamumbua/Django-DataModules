from django.shortcuts import render
from.forms import ReviewsUploadForm
from reviews.models import Reviews
from django.shortcuts import redirect

# Create your views here.
def reviews_upload_view(request):
    form =ReviewsUploadForm()
    return render(request,"reviews/reviews_upload.html",{"form":form})

def reviews_list(request):
    reviews= Reviews.objects.all()
    return render(request,"reviews/reviews_list.html",{"reviews":reviews})


def reviews_detail_view(request,id):
    reviews=Reviews.objects.all()
    return render(request,"reviews/reviews_details.html",{"reviews":reviews})

def edit_reviews_view(request,id):
    reviews=Reviews.objects.get(id=id)
    if request.method=="POST":
        form=ReviewsUploadForm(request.POST,instance=reviews)
        if form.is_valid():
            form.save()
            return redirect('reviews_detail_view',id=reviews)
        else:
            form=ReviewsUploadForm(instance=reviews)
            return render(request,'reviews/edit_reviews.html',{'form':form})