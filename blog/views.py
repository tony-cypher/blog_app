from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm

# Create your views here.


class HomePage(generic.TemplateView):
    template_name = 'index.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'


class CreatePost(generic.edit.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('home') # Redirect to this url on successful form submission


class DetailPost(generic.TemplateView):
    template_name = 'blog_detail.html'


class ContactPage(generic.TemplateView):
    template_name = 'contact.html'