from django import forms
from .models import VoltDoctors


class DocForm(forms.ModelForm):

    class Meta:
        model = VoltDoctors
        fields = (
            'name',
            'specialist',
            'from_per',
            'from_time',
            'to_time',
            'to_per',
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'إسمك'
            }),
            'specialist': forms.Select(attrs={
                'class': 'form-control',
            }),
            'from_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'من',
                'min': '1',
                'max': '12',
            }),
            'from_per': forms.Select(attrs={
                'class': 'form-control',
            }),
            'to_time': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'إلي',
                'min': '1',
                'max': '12',

            }),
            'to_per': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
