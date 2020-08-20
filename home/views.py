from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserPost, UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages


@login_required(login_url='/account/login')
def home(request):
    posts = UserPost.objects.all().order_by('-pk')
    data = {
        'posts': posts,
        'time': timezone.now()
    }
    return render(request, 'home/home.html', data)


def post(request):
    if request.method == "POST":
        user = request.user
        image = request.FILES['image']
        caption = request.POST.get('caption')
        post_object = UserPost(user=user, image=image, caption=caption)
        post_object.save()
    return redirect("/")


def delete_post(request, id):
    post = UserPost.objects.get(id=id)
    post.image.delete()
    post.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect('/')


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
    return render(request, 'home/profile.html', {'userprofile': userprofile})


def userimageUpdate(request):
    if request.method == "POST":
        image = request.FILES['image']
        userprofile = UserProfile.objects.get(user=request.user)
        if userprofile.userimage != "profiles/samplepost.png":
            userprofile.userimage.delete()
        userprofile.save()
        userprofile.userimage = image
        userprofile.save()
    return redirect("/profile/" + request.user.username)


def userimageRemove(request):
    userprofile = UserProfile.objects.get(user=request.user)
    userprofile.userimage = 'profiles/samplepost.png'
    userprofile.save()
    return redirect("/profile/" + request.user.username)
