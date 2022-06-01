from django import forms

class CalendarForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'disabled':'disabled',
                'value':'Pase normal'
            }), label='Nombre del pase')
    value = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'value':5.99
            }), label='Precio')
    reserved_date = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={
                'class':'form-control', 
                'type':'date'
            }), label='Día reservado')

class PayInfoForm(forms.Form):
    card_num = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label='Numero de tarjeta')
    exp_date = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}), label='Fecha de Expiración')
    CVC = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'max':'9999'}), label='CVC')