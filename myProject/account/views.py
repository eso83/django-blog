from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import ProfileForm


# Create your views here.


def signin_view(request):
    if request.method == 'POST':
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'password or username isnot valid')
    return render(request, 'signin.html')


def signup_view(request):
    if request.method == 'POST':
        user_name = request.POST["user_name"]
        password = request.POST["password"]
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "this user name is alrady taken!")
        else:
            User.objects.create_user(username=user_name, password=password)
            messages.success(request, 'account created,now signIn')
            return redirect('signin')

    return render(request, 'signup.html')


def signout_view(request):
    logout(request)
    return redirect('signin')


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect('home')
    return render(request, 'createPost.html')


def home_view(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'home.html', {"posts": posts})


@login_required
def profile_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {"posts": posts})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
        messages.success(request, "post deleted succesfuly!")
    else:
        massages.error(request, 'you cant delete post!')
    return redirect('profile')


@login_required
def edite_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            post.title = title
            post.content = content
            post.save()
            messages.success(request, "post deleted succesfuly!")
            return redirect("profile")
    else:
        massages.error(request, 'you cant delete post!')
        return redirect('home')
    return render(request, 'editePost.html', {'post': post})


@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'editProfile.html', {'form': form})


def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    post = Post.objects.get(id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        messages.success(request, "your like has been removed")

    else:
        post.like.add(request.user)
        messages.success(request, "you like this post")

    return redirect('home')
