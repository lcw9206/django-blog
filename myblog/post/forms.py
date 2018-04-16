# post/forms.py

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': '150자 이내로 작성해주세요'
    }))

    class Meta:
        model = Post
        fields = ['title', 'content', 'post_thumbnail']

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            title = None
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            content = None
        return content
