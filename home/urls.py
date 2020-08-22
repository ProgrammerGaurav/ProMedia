
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('post', views.post),
    path('delete_post/<int:id>', views.delete_post),
    path('like_dislike_post/<int:id>', views.like_dislike_post),
    path('follow_unfollow_user/<str:username>', views.follow_unfollow_user),
    path('profile/<str:username>', views.profile),
    path('search_user', views.search_user),
    path('liked_post/', views.liked_post),
    path('userimageUpdate', views.userimageUpdate),
    path('userimageRemove', views.userimageRemove)
]
