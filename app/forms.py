from django import forms
from .models import blogger

class BlogCommentsForm(forms.ModelForm):
    class Meta:
        model= blogger
        fields= ["title", "content", "author"]
