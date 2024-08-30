from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.models import User




# class PostAddView(request):
    # logout(request)

class PostListView(ListView):
    paginate_by = 9
    model = Post
    template_name = 'post/list.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

# create view
class PostCreateView(CreateView):
    model = Post
    template_name = 'post/create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

# update view
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post_list')

# user own posts
class UserPostListView(ListView):
    paginate_by = 15
    model = Post
    template_name = 'post/user_posts.html'
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
