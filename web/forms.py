from django import forms
from .models import Message

'''class ImageInlineForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['content', 'order']'''

class MessageForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Enter your name...',
            #'data-sb-validations': 'required'
        })
    )
    email_adress = forms.EmailField(
        widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email_adress',
        'placeholder': 'Enter your email...',
        #'data-sb-validations': 'required,email'
        })
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone_number',
            'placeholder': 'Enter your phone number...',
            #'data-sb-validations': 'required'
        })
    )
    message_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message_text',
            'placeholder': 'Enter your message...',
            #'data-sb-validations': 'required'
        })
    )
