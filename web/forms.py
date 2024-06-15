from django import forms
from .models import Publication, Image, Text

class ImageInlineForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['content', 'order']

class TextInlineForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['image', 'caption']