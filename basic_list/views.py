from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import todoListSerializer
from .models import todoList

from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

from rest_framework import viewsets




def apiOverview(request):
	api_urls = {}
	return JsonResponse(api_urls, safe=False)


   
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



class todo_list(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = todoListSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        articles = todoList.objects.all()
        serializer = todoListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)




class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer


