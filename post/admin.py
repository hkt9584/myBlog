from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author', 'created_date')
    search_fields = ('title', 'content', 'author', 'created_date')

    admin.site.register(Post)
