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

from users.models import NewUser
from .serializers import CustomUserSerializer


def apiOverview(request):
	api_urls = {}
	return JsonResponse(api_urls, safe=False)

def currentUser(request):
	api_urls = {
    "name": "Serati Ma",
    "avatar": "https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png",
    "userid": "00000001",
    "email": "antdesign@alipay.com",
}
	return JsonResponse(api_urls, safe=False) 

# def currentUser(request):
# 	class UserList(generics.ListAPIView):
#     queryset = NewUser.objects.all()
#     serializer_class = CustomUserSerializer    

def notices_list(request):
	api_urls = [
  {
      "id": "000000001",
      "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png",
      "title": "你收到了 14 份新周报",
      "datetime": "2017-08-09",
      "type": "notification"
  },
]
	return JsonResponse(api_urls, safe=False)


# @csrf_exempt
# def test_list(request):
     
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

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = basicListSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        articles = basicList.objects.all()
        serializer = basicListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)





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