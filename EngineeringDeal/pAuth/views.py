from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer,ProfileSerializer
from .models import Profile, Product


# class SignUpView(GenericAPIView):
#
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def loginApi(request,id=0):

    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     user_data = JSONParser().parse(request)
    #     user_serializer = UserSerializer(data=user_data)
    #     if user_serializer.is_valid():
    #         user_serializer.save()
    #         return JsonResponse("Added Successfully", safe=False)
    #     return JsonResponse("Failed to add", safe=False)

@csrf_exempt
def signUpApi(request, id=0):

    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
