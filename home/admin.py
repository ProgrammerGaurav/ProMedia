from django.contrib import admin
from .models import UserPost, UserProfile, Like, Following

admin.site.register(UserPost)
admin.site.register(UserProfile)
admin.site.register(Like)
admin.site.register(Following)
