from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import basicListSerializer
from .models import basicList

from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


# def apiOverview(request):
#     if request.method == 'POST':
#         api_urls = {
#             "status": "ok",
#             "currentAuthority": "admin",    
#         }
#         return JsonResponse(api_urls, safe=False)
#     return JsonResponse(serializer.errors, status=400)


# def basic_list(request):
     
#     if request.method == 'GET':
#         articles = basicList.objects.all()
#         serializer = basicListSerializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = basicListSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             articles = basicList.objects.all()
#             serializer = basicListSerializer(articles, many=True)
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors, status=400)

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class basic_list(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = basicList.objects.all()
    serializer_class = basicListSerializer


class basic_listDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = basicList.objects.all()
    serializer_class = basicListSerializer