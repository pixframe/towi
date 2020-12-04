from django import forms
from django.contrib.admin import widgets 
from .models import Suscription, SuscriptionType
from accounts.models import User


class SuscriptionForm(forms.ModelForm):

    class Meta:
        model = Suscription
        fields = '__all__'


class SuscriptionsFormAdmin(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    type_subs = forms.ModelChoiceField(queryset=SuscriptionType.objects.all())
    init_date = forms.SplitDateTimeField(
        label="Fecha Inicial", 
        widget=widgets.AdminSplitDateTime()
    )
    end_date = forms.SplitDateTimeField(
        label="Fecha final", 
        widget=widgets.AdminSplitDateTime()
    )
    suscriptions = forms.IntegerField(label="suscripciones",)