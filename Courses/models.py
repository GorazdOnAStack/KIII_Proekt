from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=50, default='Java')
    url= EmbedVideoField(blank=True)
    body = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title +' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
