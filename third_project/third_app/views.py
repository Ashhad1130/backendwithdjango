from django.shortcuts import render
from third_app.forms import UserForm,UserProfileInfoForm,CommentForm
# Create your views here.
from third_app.models import Comment
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import resolve



def index(request):

    return render(request,'third_app/index.html')

def details(request):
    return render(request,'third_app/details.html')
def login(request):
    return render(request,'third_app/login.html')
def story1(request):
    global newpost
    newpost=request.path
    return render(request,'third_app/story1.html')

def register(request):
    registered=False
    profiles=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pics' in request.FILES:
                profile.profile_pics=request.FILES['profile_pics']
                profiles=True
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'third_app/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required
def special(request):
    return HttpResponse("You are Logged in")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                auth_login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password {}".format(username,password))
            return HttpResponse("Invalid Login details given")
    else:
        return render(request,'third_app/login.html')



def post_detail(request):
    newposter=newpost.split('/')
    post=newposter[-1]
    if request.method=="POST":
        post_t=str(post)
        print(post_t)
        comment_form=CommentForm(data=request.POST)
        if comment_form.is_valid():
            content=request.POST.get("content")
            comments=Comment.objects.create(content=content,user=request.user,post_title=post_t)
            comments.save()
            comments=Comment.objects.filter(post_title=post_t)
            print(comments)


        else:
            print(comment_form.errors)
    else:
        comment_form=CommentForm()
    #return HttpResponseRedirect(newpost)
    return render(request,'third_app/story1.html',{'comments':comments})
