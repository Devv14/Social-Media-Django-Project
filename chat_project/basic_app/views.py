from django.contrib.auth.base_user import AbstractBaseUser
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.auth.models import Group, User
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from basic_app import models
from django.utils import timezone

# LOGIN REQUIRED
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# LOGIN-LOGOUT
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# SIGNUP
from basic_app import forms
from basic_app.models import MyGroup
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'basic_app/signup_form.html'
    success_url = reverse_lazy('basic_app:login')
    # fields = ('username','email','password')
    # model = User

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            # user.is_authenticated = True
            login(request,user)
            return redirect('basic_app:user')
        else:
            # we'll have to create messages in the apps base.html file
            messages.success(request,("There was an error logging in, Try Again.."))
            return redirect('basic_app:login')
    else:
        return render(request,'basic_app/login.html')

class LoginLandingView(LoginRequiredMixin,TemplateView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    template_name = 'basic_app/login_land.html'

@login_required
def logout_user(request):
    # list = models.MyGroup.objects.filter(join_click=True)
    # for i in range(len(list)):
    #     group = list[i]
    #     group.join_click=False
    #     group.save()
    logout(request)
    messages.success(request,("You were logged out"))
    return redirect('home')

# class LogoutReferenceView(LoginRequiredMixin,ListView):
#     login_url = '/basic_app/login/'
#     redirect_field_name = 'login'
#     context_object_name = 'groups'
#     model = models.MyGroup
#     template_name = 'basic_app/logout_reference.html'


class PostView(LoginRequiredMixin,CreateView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    form_class = forms.MyPostForm
    # NO NEED TO SPECIFY FIELD HERE
    # fields = ('mssg','group')
    model = models.MyPost

class GroupView(LoginRequiredMixin,CreateView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    form_class = forms.MyGroupForm
    model = models.MyGroup

class GroupListView(LoginRequiredMixin,ListView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    model = models.MyGroup
    context_object_name = 'groups'

class JoinDetailView(LoginRequiredMixin,DetailView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    context_object_name = 'group_detail'
    model = models.MyGroup
    template_name = 'basic_app/join_detail.html'

@login_required
def leave_view(request,pk):
    group = get_object_or_404(models.MyGroup,pk=pk)
    of = group.member_count
    nf = of+1
    group.member_count = nf
    group.add_string += request.user.username
    group.on_click()
    group.save()
    return redirect('basic_app:join',pk=group.pk)

@login_required
def joinback_view(request,pk):
    group = get_object_or_404(models.MyGroup,pk=pk)
    of = group.member_count
    nf = of-1
    group.member_count = nf
    group.remove_string += request.user.username
    group.return_click()
    group.save()
    return redirect('basic_app:join',pk=group.pk)

class PostsInGroupView(LoginRequiredMixin,DetailView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    context_object_name = 'group_detail'
    model = models.MyGroup
    template_name = 'basic_app/post_in_group.html' 

class DeleteOptionPage(LoginRequiredMixin,DeleteView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    # we chose MyPost model as we are referring to single post
    template_name = 'basic_app/mypost_confirm_delete.html'
    context_object_name = 'post'
    model = models.MyPost

    def get_success_url(self):
        return reverse_lazy('basic_app:postdeletebts', kwargs={'pk': self.object.group.pk})

class AllPostsView(LoginRequiredMixin,ListView):
    login_url = '/basic_app/login/'
    redirect_field_name = 'login'
    context_object_name = 'groups'
    model = models.MyGroup
    template_name = 'basic_app/allposts_general.html'

@login_required
def nondisplay_view(request,pk):
    post = get_object_or_404(models.MyPost,pk=pk)
    post.created_by=request.user.username
    post.group.post_count=post.group.post_count+1
    post.save()
    post.group.save()
    return redirect('basic_app:postsingroup',pk=post.group.pk)

@login_required
def post_deleteview(request,pk):
    group = get_object_or_404(models.MyGroup,pk=pk)
    group.post_count=group.post_count-1
    group.save()
    return redirect('basic_app:allposts')

class BaseGroupDisplayView(ListView):
    context_object_name = 'groups'
    model = models.MyGroup
    template_name = 'homegroups.html'

@login_required
def grab_userview(request,pk):
    post = get_object_or_404(models.MyPost,pk=pk)
    list = models.MyPost.objects.filter(created_by=post.created_by)
    dict = {'list':list,'postcreator':post.created_by}
    return render(request,'basic_app/user_posts.html',context=dict)