from django import forms

from .models import  Tab
class TabForm(forms.ModelForm):
    class Meta:
        model= Tab
        fields=[
            'name',
            'brand',
            'Processor',
            'Camera',
            'price'

        ]
