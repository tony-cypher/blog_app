from django.shortcuts import render
from django.views import generic

# Create your views here.


class HomePage(generic.TemplateView):
    template_name = 'index.html'


class AboutPage(generic.TemplateView):
    template_name = 'about.html'


class DetailPage(generic.TemplateView):
    template_name = 'blog_detail.html'


class ContactPage(generic.TemplateView):
    template_name = 'contact.html'