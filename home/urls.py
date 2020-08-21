
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('post', views.post),
    path('delete_post/<int:id>', views.delete_post),
    path('like_dislike_post/<int:id>', views.like_dislike_post),
    path('profile/<str:username>', views.profile),
    path('userimageUpdate', views.userimageUpdate),
    path('userimageRemove', views.userimageRemove)
]
