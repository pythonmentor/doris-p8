from django_select2.forms import Select2Widget
from django import forms

class SearchForm(forms.Form):
    product = forms.CharField(widget = Select2Widget)
