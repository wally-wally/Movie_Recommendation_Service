from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    score = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Comment
        fields = ('score', 'content',)