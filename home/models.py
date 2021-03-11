from django.db import models
from django.contrib.auth.models import User
import os
from allauth.account.signals import user_signed_up
from cloudinary.models import CloudinaryField


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=20000)
    image = CloudinaryField('image', folder="promedia/post")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    userimage = CloudinaryField('image', folder="promedia/profiles",
                                default="image/upload/v1615479030/promedia/profiles/defauly_qtracn.png")
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
        return str(self.post)


class Following(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followed = models.ManyToManyField(User, related_name="followed")

    @classmethod
    def follow(cls, user, follow_user):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.add(follow_user)

    @classmethod
    def unfollow(cls, user, unfollow_user):
        obj, create = cls.objects.get_or_create(user=user)
        obj.followed.remove(unfollow_user)

    def __str__(self):
        return str(self.user)
