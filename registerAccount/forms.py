from django import forms
from.models import RegisterAccount
class RegisterAccountUploadForm(forms.ModelForm):
    class Meta:
        model= RegisterAccount
        fields= "__all__"