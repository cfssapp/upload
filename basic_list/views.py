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

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


@csrf_exempt
@api_view(['GET'])
def apiOverview(request):
	api_urls = [{
        "logo": "https://64.media.tumblr.com/avatar_84bf27cec37f_128.pnj",
        "title": "Albert Einstein",
        "href": "https://www.google.com.my/",
        "subDescription": "Imagination is more important than knowledge",
        
        "owner": "User",
        "createdAt": 1607155074056,
        "updatedAt": 1607155074056,
        "percent": 83,
        "status": "active", 
    }] 
	return JsonResponse(api_urls, safe=False)


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




class basic_list(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = basicList.objects.all()
    serializer_class = basicListSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['user_name'] = self.user.user_name
        data['is_active'] = self.user.is_active
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer