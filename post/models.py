from django.db import models

class Post(models.Model):
    title = models.CharField('標題', max_length=20)
    content = models.CharField('內容', max_length=300)
