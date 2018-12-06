from django import forms

class SearchForm(forms.Form):
    product = forms.CharField(label = 'product')
