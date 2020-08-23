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


@csrf_exempt
def user(request):
    if request.method == "GET":
        try:
            user = User.objects.get(username=str(request.user))
        except:
            return JsonResponse({"Logged In": False})
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        user = User.objects.get(username=str(data['username']))
        user.email = data['email']
        user.save()
        serializer = UserSerializer(user, many=False)
        return JsonResponse(serializer.data)
