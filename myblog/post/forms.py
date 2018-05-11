# post/forms.py

from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': '150자 이내로 작성해주세요'
    }))

    class Meta:
        model = Post
        fields = ['title', 'content', 'post_thumbnail', 'category']

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


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': '댓글을 입력해주세요.',
        'class': 'comment-form',
    }))

    class Meta:
        model = Comment
        fields = ['content']
