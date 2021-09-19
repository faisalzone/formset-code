from django.forms import ModelForm
from .models import Example


class ExampleForm(ModelForm):
    class Meta:
        model = Example
        fields = ['name', 'location', 'photo']
        labels = {'name': 'Name'}
