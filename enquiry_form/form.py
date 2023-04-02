from django import forms
from django.forms import ModelForm
from .models import EnquiryForm


class UpdateInquiery(ModelForm):
    class Meta:
        model = EnquiryForm
        fields = ('first_name', 'last_name', 'city', 'email', 'comment')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'last_name'}),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                    'placeholder': 'city'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                      'placeholder': 'Email :ex. example@info.com'}),
            'comment': forms.Textarea(attrs={'class': 'form-control',
                                      'placeholder': 'Write message'}),
            
        }
