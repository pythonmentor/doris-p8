from django import forms

class ConnectionForm(forms.Form):
    email = forms.EmailField(label = "Email")
    password = forms.CharField(label = "Mot de passe", widget=forms.PasswordInput, max_length=150)
