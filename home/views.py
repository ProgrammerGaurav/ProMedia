from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserPost, UserProfile, Like
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages
import json


@login_required(login_url='/account/login')
def home(request):
    posts = UserPost.objects.all().order_by('-pk')
    liked_post = [post for post in posts if Like.objects.filter(
        post=post, user=request.user)]
    data = {
        'posts': posts,
        'time': timezone.now(),
        'liked_post': liked_post
    }
    print(liked_post)
    return render(request, 'home/home.html', data)


def post(request):
    if request.method == "POST":
        user = request.user
        image = request.FILES['image']
        caption = request.POST.get('caption')
        post_object = UserPost(user=user, image=image, caption=caption)
        post_object.save()
        messages.success(request, "Post Uploaded Sucessfully")
    return redirect("/")


def delete_post(request, id):
    post = UserPost.objects.get(id=id)
    post.image.delete()
    post.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('/')


def like_dislike_post(request, id):
    post = UserPost.objects.get(id=id)
    like = Like.objects.filter(post=post, user=request.user)
    liked = False
    if like:
        Like.dislike(post, request.user)
    else:
        liked = True
        Like.like(post, request.user)
    data = {
        'liked': liked
    }
    response = json.dumps(data)
    return HttpResponse(response, content_type="application/json")


def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        messages.warning(request, "User Not Found")
        return redirect("/")
    userprofile = UserProfile.objects.filter(user=user)
    if not userprofile:
        userprofile = UserProfile(user=user)
        userprofile.save()
    userprofile = UserProfile.objects.get(user=user)
    posts = UserPost.objects.filter(user=user).order_by('-pk')
    data = {
        'userprofile': userprofile,
        'posts': posts,
        'time': timezone.now()
    }
    return render(request, 'home/profile.html', data)


def userimageUpdate(request):
    if request.method == "POST":
        image = request.FILES['image']
        userprofile = UserProfile.objects.get(user=request.user)
        if str(userprofile.userimage) != "profiles/samplepost.png":
            userprofile.userimage.delete()
        userprofile.save()
        userprofile.userimage = image
        userprofile.save()
    return redirect("/profile/" + request.user.username)


def userimageRemove(request):
    userprofile = UserProfile.objects.get(user=request.user)
    if str(userprofile.userimage) != "profiles/samplepost.png":
        userprofile.userimage.delete()
    userprofile.userimage = 'profiles/samplepost.png'
    userprofile.save()
    return redirect("/profile/" + request.user.username)
