from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm

# Create your views here.


class HomePage(TemplateView):
    template_name = 'index.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('home') # Redirect to this url on successful form submission

    def form_invalid(self, form):
        # prints form errors to the console
        print(form.errors)
        # You can add additional handling for form validation errors if needed
        return super().form_invalid(form)



class DetailPost(TemplateView):
    template_name = 'blog_detail.html'


class ContactPage(TemplateView):
    template_name = 'contact.html'