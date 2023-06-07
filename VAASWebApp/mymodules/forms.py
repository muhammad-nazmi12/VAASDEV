from django import forms
from VAASWebApp.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=('name','document')