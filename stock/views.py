from django.shortcuts import render
from.forms import StockUploadForm
from stock.models import Stock
from django.shortcuts import redirect

# Create your views here.
def stock_upload_view(request):
    form =StockUploadForm()
    return render(request,"stock/stock_upload.html",{"form":form})

def stock_list(request):
    stock= Stock.objects.all()
    return render(request,"stock/stock_list.html",{"stock":stock})

def stock_detail_view(request):
    stock= Stock.objects.all()
    return render(request,"stock/stock_detail.html",{"stock":stock})

def edit_stock_view(request,id):
    stock=Stock.objects.get(id=id)
    if request.method=="POST":
        form=StockUploadForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_detail_view',id=stock)
        else:
            form=StockUploadForm(instance=stock)
            return render(request,'stock/edit_stock.html',{'form':form})