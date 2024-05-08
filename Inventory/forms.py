from .models import Product,Purchase
from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','quantity','company','unit','image','due_date']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        