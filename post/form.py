from django import forms
from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control summernote'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control'}),
            # 'created_date': forms.TextInput(attrs={'class': 'form-control'}),
        }

    @login_required
    @permission_required('post.add_post')
    def post_create(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request, "文章新增成功")
                return redirect('post_detail', pk=post.pk)
            else:
                messages.error(request, "文章新增失敗")
        else:
            form = PostForm()
        return render(request, 'post/create.html', {'form': form, 'errors': form.errors})
    
    @login_required
    @permission_required('post.change_post')
    def post_update(request, pk):
        post = Post.objects.get(pk=pk)
        # Check if the current user is the author of the post
        if post.author != request.user.username:
            messages.warning(request, "您無權修改此文章")
            return redirect('post_detail', pk=post.pk)
        
        errors = None  # Initialize errors variable
        
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                messages.success(request, "文章修改成功")
                return redirect('post_detail', pk=post.pk)
            else:
                errors = form.errors
                messages.error(request, "文章修改失敗")
        else:
            form = PostForm(instance=post)
            
        return render(request, 'post/update.html', {'form': form, 'errors': errors})
    
    @login_required
    @permission_required('post.delete_post')
    def post_delete(request, pk):
        post = Post.objects.get(pk=pk)
        # Check if the current user is the author of the post
        if post.author != request.user.username:
            return redirect('post_detail', pk=post.pk)
        post.delete()
        messages.success(request, "文章刪除成功")
        return redirect('user_posts')
    
