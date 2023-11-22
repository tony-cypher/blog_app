from .models import Post, Comment, Team, Contact
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category', 'img',]
        widgets = {
            'author': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea', 'placeholder':'Post Details'}),
            'img': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter your email'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment'})
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('first_name', 'last_name', 'category', 'description', 'pics')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Last Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'pics': forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}),
            'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}),
        }