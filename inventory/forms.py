from django import forms
from.models import Inventory
class ProductUploadForm(forms.ModelForm):
    class Meta:
        model= Inventory
        fields= "__all__"