from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin

class Post(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    title = models.CharField('標題', max_length=20)
    content = models.CharField('內容', max_length=300)
    author = models.CharField('作者', max_length=20,default='SOME STRING', blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'author')
    search_fields = ('title', 'content', 'author', 'created_date')
     