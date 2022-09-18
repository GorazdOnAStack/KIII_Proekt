from django.urls import path
from . import views
from .views import soloPost, AddPost, AddCommentt

urlpatterns = [
    path("",views.home, name="home"),
    path("register/",views.register,name="register"),
    path("login/",views.loginP,name="login"),
    path("logout/",views.logoutUser,name="logout"),
    path("post/<int:pk>", soloPost.as_view(),name='solopost'),
    path("addpost/",AddPost.as_view(),name="addpost"),
    path('post/<int:pk>/comment',AddCommentt.as_view(),name='addcomment'),
    path("java/",views.java, name="java"),
    path("cee/",views.cee, name="cee"),
    path("cplus/",views.cplus, name="cplus"),
    path("boot_strap/",views.boot_strap, name="boot_strap"),
    path("java_script/",views.java_script, name="java_script"),
    path("html5/",views.html5, name="html5"),
]