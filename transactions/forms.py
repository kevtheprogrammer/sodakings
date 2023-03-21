from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import *

class PurchaseBillForm(ModelForm):
    class Meta:
        model = PurchaseBill 
        fields = (
            'supplier',
			'destination', 
			'po', 'cgst', 'igst', 'cess','tcs', 
        )
        
        widgets = {
            'supplier': forms.RadioSelect(),
            'po': forms.ClearableFileInput(),
		}

 