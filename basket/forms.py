from django import forms
from.models import Basket
class BasketUploadForm(forms.ModelForm):
    class Meta:
        model= Basket
        fields= "__all__"