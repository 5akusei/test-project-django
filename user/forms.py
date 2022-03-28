from dataclasses import fields
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username','password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].label = 'Correo'
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'] = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Contraseña')
        self.fields['conf_password'] = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Repita la contraseña')