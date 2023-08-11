from django import forms
from.models import Stock
class StockUploadForm(forms.ModelForm):
    class Meta:
        model= Stock
        fields= "__all__"