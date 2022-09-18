from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from multiprocessing import context
from urllib import request
from .forms import CreateUserForm, PostForm, CommentForm
from .models import Post, Comment

# Create your views here.
def home(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"home.html",context)

def register(request):    
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('login')

    context={'form':form}
    return render(request,"register.html",context)

def loginP(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password isn\'t matching')

    context={}
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    return redirect('home')

class soloPost(DetailView):
    model = Post
    template_name = "post.html"
    
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "AddPost.html"
    #fields ="__all__"

class AddCommentt(CreateView):
    model = Post
    form_class = CommentForm
    template_name = "add_comment.html"
    success_url = reverse_lazy('home')
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    #fields ="__all__"    


def java(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"java.html",context)

def cplus(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"cplus.html",context)

def cee(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"cee.html",context)

def java_script(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"java_script.html",context)    

def html5(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"html5.html",context)

def boot_strap(request):
    model = Post.objects.all
    context ={'posts':model}
    return render(request,"boot_strap.html",context)