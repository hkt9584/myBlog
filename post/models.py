from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField('標題', max_length=20)
    content = models.CharField('內容', max_length=300)
    author = models.CharField(max_length=20,default='SOME STRING')
    created_date = models.DateTimeField(default=timezone.now)