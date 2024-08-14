from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

from django.contrib.auth import logout

# class PostAddView(request):
    # logout(request)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'