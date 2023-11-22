from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView, TemplateView, ListView
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Team, Contact
from .forms import PostForm, TeamForm, ContactForm, CommentForm

# Create your views here.


class HomePage(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'

    def get_queryset(self):
        all_posts = Post.objects.all()
        trending = all_posts[:5]
        first_posts = all_posts[:3]
        second_posts = all_posts[3:6]
        culture_posts = Post.objects.filter(category='culture', published__lte=timezone.now()).order_by('-published')[:3]
        business_posts = Post.objects.filter(category='business', published__lte=timezone.now()).order_by('-published')[:3]
        culture_x = culture_posts[0]
        culture_y = culture_posts[1]
        culture_z = culture_posts[2]
        business_x = business_posts[0]
        business_y = business_posts[1]
        business_z = business_posts[2]
        return {
            'trending': trending, 'first_posts':first_posts, 'second_posts':second_posts,
            'culture_posts':culture_posts, 'business_posts':business_posts, 'culture_x':culture_x,
            'culture_y':culture_y, 'culture_z':culture_z, 'business_x':business_x, 'business_y':business_y,
            'business_z':business_z
        }    

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
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


def post_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'form': form})

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
    return redirect('draft')

@login_required
def comment_approve(request, slug, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve_comment()
    return redirect('detail', slug=slug)


@login_required
def comment_delete(request, slug, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', slug=slug)

