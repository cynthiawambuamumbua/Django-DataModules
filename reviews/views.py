from django.shortcuts import render
from.forms import ReviewsUploadForm
# from inventory.models import Product
# from django.shortcuts import redirect

# Create your views here.
def reviews_upload_view(request):
    form =ReviewsUploadForm()
    return render(request,"reviews/reviews_upload.html",{"form":form})