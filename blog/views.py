from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Team, Contact
from .forms import PostForm, TeamForm, ContactForm

# Create your views here.


class HomePage(TemplateView):
    template_name = 'index.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('home') # Redirect to this url on successful form submission


class DraftPost(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_draft.html'

    def get_quertset(self):
        return Post.objects.filter(published__isnull = True).order_by('created')
    

class DetailPost(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutPage(ListView):
    model = Team
    context_object_name = 'team'
    template_name = 'about.html'

class CreateTeam(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'team_form.html'
    success_url = reverse_lazy('about')


class ContactPage(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')


@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('home')