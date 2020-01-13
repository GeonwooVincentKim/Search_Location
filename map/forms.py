from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # id = forms.CharField(max_length=100)
        # title = forms.CharField(max_length=40)
        # created_at = forms.DateTimeField()
        # updated_at = forms.DateTimeField()
        model = Post
        fields = ['title', 'lnglat']
