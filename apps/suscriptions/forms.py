from django import forms
from .models import Suscription


class SuscriptionForm(forms.ModelForm):

    class Meta:
        model = Suscription
        fields = '__all__'
