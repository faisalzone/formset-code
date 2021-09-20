from django.forms import ModelForm, formset_factory
from .models import Example
from django import forms

class ExampleForm(ModelForm):
    class Meta:
        model = Example
        fields = ['name', 'location', 'photo']
        labels = {'name': 'Name'}


class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )


BookFormset = formset_factory(BookForm, extra=1)
