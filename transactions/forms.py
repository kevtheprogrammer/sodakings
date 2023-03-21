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
            'po': forms.ClearableFileInput(),
		}


class PurchaseItemForm(ModelForm):
    class Meta:
        model = PurchaseItem 
        fields = (
			'stock', 
			'quantity', 'perprice', 'totalprice',  
        )
      
class SaleBillForm(ModelForm):
    class Meta:
        model = SaleBill 
        fields = (
			'gstin', 'customer',
			'destination', 'po', 'cgst', 'sgst', 'igst', 'cess','tcs'
        )


class SaleItemForm(ModelForm):
    class Meta:
        model = SaleItem 
        fields = (
			'stock', 
			'quantity', 'perprice', 'totalprice',  
        )