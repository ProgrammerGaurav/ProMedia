from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserPost, UserProfile, Like, Following
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


def follow_unfollow_user(request, username):
    follow_user = User.objects.get(username=username)
    is_following = Following.objects.filter(
        user=request.user, followed=follow_user)
    followed = False
    if is_following:
        Following.unfollow(request.user, follow_user)
    else:
        followed = True
        Following.follow(request.user, follow_user)
    data = {
        'followed': followed
    }
    response = json.dumps(data)
    return HttpResponse(response, content_type="application/json")


@login_required(login_url='/account/login')
def profile(request, username):
    try:
        userprofile = UserProfile.objects.create(user=request.user)
        following = Following.objects.create(user=request.user)
    except:
        pass
    try:
        user = User.objects.get(username=username)
    except:
        messages.warning(request, "User Not Found")
        return redirect("/")
    #
    userprofile = UserProfile.objects.filter(user=user)
    following_obj = Following.objects.get(user=user)
    #
    userprofile = UserProfile.objects.get(user=user)
    userprofile.following = following_obj.followed.count()
    # followers
    followers = 0
    following_objs = Following.objects.all()
    for following_obj in following_objs:
        followers += following_obj.followed.filter(username=user).count()
    userprofile.followers = followers
    userprofile.save()
    #
    posts = UserPost.objects.filter(user=user).order_by('-pk')
    liked_post = [post for post in posts if Like.objects.filter(
        post=post, user=request.user)]
    #
    is_following = Following.objects.filter(user=request.user, followed=user)
    if is_following:
        is_following = True
    else:
        is_following = False
    data = {
        'userprofile': userprofile,
        'posts': posts,
        'time': timezone.now(),
        'is_following': is_following,
        'liked_post': liked_post
    }
    return render(request, 'home/profile.html', data)


def search_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        userprofiles = []
        userss = User.objects.filter(username__icontains=username)
        for users in userss:
            userprofiles.append(UserProfile.objects.get(user=users))
    data = {'userprofiles': userprofiles}
    if userprofiles:
        return render(request, 'home/searchuser.html', data)
    else:
        messages.warning(request, "No user found")
        return redirect("/")


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


def liked_post(request):
    likes = Like.objects.all()
    posts = []
    for like in likes:
        if request.user in like.user.all():
            posts.append(like.post)
    liked_post = [post for post in posts if Like.objects.filter(
        post=post, user=request.user)]
    data = {
        'posts': posts,
        'time': timezone.now(),
        'liked_post': liked_post
    }
    return render(request, 'home/likedpost.html', data)


def useredit(request):
    if request.method == "POST":
        username = request.POST.get('username')
        bio = request.POST.get('bio', '')
        links = request.POST.get('links', '')
    userprofile = UserProfile.objects.get(user=request.user)
    user = User.objects.get(username=request.user.username)
    user.username = username
    user.save()
    userprofile.user.save()
    userprofile.bio = bio
    userprofile.connection = links
    userprofile.save()
    return redirect("/profile/" + str(username))
