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



def apiOverview(request):
	api_urls = {
    "name": "Serati Ma",
    "avatar": "https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png",
    "userid": "00000001",
    "email": "antdesign@alipay.com",
    "signature": "海纳百川，有容乃大",
    "title": "交互专家",
    "group": "蚂蚁集团－某某某事业群－某某平台部－某某技术部－UED",
    "tags": [
        {
            "key": "0",
            "label": "很有想法的"
        },
        {
            "key": "1",
            "label": "专注设计"
        },
        {
            "key": "2",
            "label": "辣~"
        },
        {
            "key": "3",
            "label": "大长腿"
        },
        {
            "key": "4",
            "label": "川妹子"
        },
        {
            "key": "5",
            "label": "海纳百川"
        }
    ],
    "notifyCount": 12,
    "unreadCount": 11,
    "country": "China",
    "geographic": {
        "province": {
            "label": "浙江省",
            "key": "330000"
        },
        "city": {
            "label": "杭州市",
            "key": "330100"
        }
    },
    "address": "西湖区工专路 77 号",
    "phone": "0752-268888888"
}
	return JsonResponse(api_urls, safe=False)

def currentUser(request):
	api_urls = {
    "name": "Serati Ma",
    "avatar": "https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png",
    "userid": "00000001",
    "email": "antdesign@alipay.com",
    "signature": "海纳百川，有容乃大",
    "title": "交互专家",
    "group": "蚂蚁集团－某某某事业群－某某平台部－某某技术部－UED",
    "tags": [
        {
            "key": "0",
            "label": "很有想法的"
        },
        {
            "key": "1",
            "label": "专注设计"
        },
        {
            "key": "2",
            "label": "辣~"
        },
        {
            "key": "3",
            "label": "大长腿"
        },
        {
            "key": "4",
            "label": "川妹子"
        },
        {
            "key": "5",
            "label": "海纳百川"
        }
    ],
    "notifyCount": 12,
    "unreadCount": 11,
    "country": "China",
    "geographic": {
        "province": {
            "label": "浙江省",
            "key": "330000"
        },
        "city": {
            "label": "杭州市",
            "key": "330100"
        }
    },
    "address": "西湖区工专路 77 号",
    "phone": "0752-268888888"
}
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