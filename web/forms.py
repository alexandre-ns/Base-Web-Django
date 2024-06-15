from django import forms
from .models import Publication, Image, Text

class ImageInlineForm(forms.ModelForm):
    class Meta:
        model = Secundario1
        fields = ['content', 'order']

'''class TextInlineForm(forms.ModelForm):
    class Meta:
        model = Secundario2
        fields = ['image', 'caption']'''