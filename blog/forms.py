from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category', 'img',]
        widgets = {
            'author': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Post Details'}),
            'img': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')