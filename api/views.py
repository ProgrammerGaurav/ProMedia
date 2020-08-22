from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from home.models import UserPost
from .serializers import *
from django.contrib.auth.models import User


@csrf_exempt
def userpost(request):
    if request.method == 'GET':
        posts = UserPost.objects.all()
        serializer = UserPostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@login_required(login_url='/account/login')
def user(request):
    if request.method == "GET":
        user = User.objects.get(username=str(request.user))
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data)
