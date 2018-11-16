from django import forms
from products.models import Product

class SearchForm(forms.Form):
    product = forms.CharField()
