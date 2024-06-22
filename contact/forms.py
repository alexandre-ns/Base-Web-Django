from django import forms
from .models import Message

# Form for user submitted messages on the contact.html page
class MessageForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'digite seu nome',
            #'data-sb-validations': 'required'
        }),
        label="Nome"
    )
    email_adress = forms.EmailField(
        widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email_adress',
        'placeholder': 'Insira endereço de email',
        #'data-sb-validations': 'required,email'
        }),
        label="Email"
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone_number',
            'placeholder': 'Insira número de telefone',
            #'data-sb-validations': 'required'
        }),
        label="Telefone"
    )
    message_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'message_text',
            'placeholder': 'Digite sua mensagem',
            #'data-sb-validations': 'required'
        }),
        label="Mensagem"
    )
