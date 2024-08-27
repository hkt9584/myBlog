from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

from django.contrib.auth import logout

from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.models import User




# class PostAddView(request):
    # logout(request)

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# class PostAddlView(AddView):
    # model = Post
    # template_name = 'add_post.html'

def add_post(request):
    if request.method == "POST" :       
        post_form = PostForm (request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = User.objects.get(pk=1)
            new_post.save()
            return redirect("post:post_list")
        else:
            return HttpResponse("内容有誤，請重寫")  
    else:
        
        post_form = PostForm()
        context = {'post_form' : post_form }
        return render(request,'add_post.html',context)

   