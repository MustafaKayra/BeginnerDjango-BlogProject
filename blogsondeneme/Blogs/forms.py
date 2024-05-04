from django import forms
from .models import Blog

class BlogForm(forms.ModelForm): # Form for adding blog
    class Meta:
        model = Blog # take the Blog model
        fields = ["title","content","image"] # Fields required to add blog