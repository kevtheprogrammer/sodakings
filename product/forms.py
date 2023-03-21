from django import forms

from .models import * 

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = (
            'thumb',
            'name',
            'price',
            'description',
            'slug',
        )
    
class StockForm(forms.ModelForm):
    class Meta:
        model = StockModel
        fields = (
            'name',
            'prod',
            'quantity',
            'slug',
        )
        widgets = {
            'prod': forms.RadioSelect(),
        }
    
