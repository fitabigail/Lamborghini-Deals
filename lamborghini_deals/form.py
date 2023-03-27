from django import forms
from django.forms import ModelForm
from .models import Contact

# Create contact form here.


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'phone', 'message')

        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'phone': '',
            'message': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Subject'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone :ex. +12345678901'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write message'}),
            
        }