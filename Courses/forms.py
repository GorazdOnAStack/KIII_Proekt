from dataclasses import field, fields
from tkinter.ttk import Widget
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment,Category

cats = Category.objects.all().values_list('name','name')
cat_list=[]
for cat in cats:
    cat_list.append(cat)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","author","category","url","body")

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control','id':'uname'}),
            'category': forms.Select(choices=cats,attrs={'class':'form-control'}),
            'url': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ('name','body')
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'user_name','value':''}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }