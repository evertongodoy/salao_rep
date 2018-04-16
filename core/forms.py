from django import forms

class AreaRestritaCore(forms.Form):

    user = forms.CharField(label='Nome', max_length=100)
    password = forms.CharField(
        label='Senha', max_length=32, widget=forms.PasswordInput
    )