from django.db import models
from django.contrib.auth.models import User
import os


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=20)
    image = models.ImageField(upload_to="post/")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    userimage = models.ImageField(
        upload_to="profiles/", default="profiles/samplepost.png")
    bio = models.CharField(max_length=300, blank=True)
    connection = models.CharField(max_length=100, blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Like(models.Model):
    user = models.ManyToManyField(User)
    post = models.OneToOneField(UserPost, on_delete=models.CASCADE)

    @classmethod
    def like(cls, post, like_user):
        obj, create = cls.objects.get_or_create(post=post)
        obj.user.add(like_user)

    @classmethod
    def dislike(cls, post, dislike_user):
        obj, create = cls.objects.get_or_create(post=post)
        obj.user.remove(dislike_user)

    def __str__(self):
        return self.user.username
