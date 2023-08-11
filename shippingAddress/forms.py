from django import forms
from.models import ShippingAddress
class ShippingAddressUploadForm(forms.ModelForm):
    class Meta:
        model= ShippingAddress
        fields= "__all__"