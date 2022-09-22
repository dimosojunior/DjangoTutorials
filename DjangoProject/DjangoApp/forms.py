from .models import *
from django.forms import ModelForm
from django import forms

class ProductsForm(forms.ModelForm):
    	
    class Meta:
        model = Products
        fields = '__all__'
        #fields =['name', 'price', 'brand']
        
class UpdateProductsForm(forms.ModelForm):
    	
    class Meta:
        model = Products
        fields = '__all__'
        #fields =['name', 'price', 'brand']