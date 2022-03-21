from django import forms
from zoo.models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['type_of_bird']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['size'].widget.attrs.update({'class': "form-control form-select"})
        self.fields['size'].empty_label = 'Escoja un tamaño'
        self.fields['life_span'].widget.attrs.update({'class': 'form-control', 'max':'150', 'min':'1'})
        self.fields['family'].widget.attrs.update({'class': 'form-control'})