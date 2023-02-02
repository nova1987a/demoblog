from .models import BlogComment
from django import forms

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']

