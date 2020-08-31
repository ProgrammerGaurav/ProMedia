from django.urls import path, include
from . import views
import rest_auth


urlpatterns = [
    path('user/', views.user),
    path('userpost/', views.userpost),
    path('userprofile/<str:username>', views.userprofile),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
