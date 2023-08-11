from django.shortcuts import render
from.forms import ReviewsUploadForm
from reviews.models import Reviews
# from django.shortcuts import redirect

# Create your views here.
def reviews_upload_view(request):
    form =ReviewsUploadForm()
    return render(request,"reviews/reviews_upload.html",{"form":form})

def reviews_list(request):
    reviews= Reviews.objects.all()
    return render(request,"reviews/reviews_list.html",{"reviews":reviews})