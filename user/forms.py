from dataclasses import fields
from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Correo')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Contraseña')

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

class UserFormUpdate(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','username','is_admin','is_active','is_staff']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].label = 'Correo'
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['is_admin'].widget.attrs.update({'class': "form-check-input"})
        self.fields['is_active'].widget.attrs.update({'class': "form-check-input"})
        self.fields['is_staff'].widget.attrs.update({'class': "form-check-input"})

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email','username','password1','password2')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].widget.attrs.update({'class': 'form-control'})
#         self.fields['email'].label = 'Correo'
#         self.fields['username'].widget.attrs.update({'class': 'form-control'})
#         self.fields['username'].label = 'Nombre de usuario'
#         self.fields['password1'].widget.attrs.update({'class': 'form-control'})
#         self.fields['password2'].widget.attrs.update({'class': 'form-control'})