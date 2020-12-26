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

from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404




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


# class PostList(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = todoList.objects.all()
#     serializer_class = todoListSerializer


# class PostDetail(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = todoList.objects.all()
#     serializer_class = todoListSerializer


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = todoListSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(todoList, id=item)

#     # Define Custom Queryset
#     def get_queryset(self):
#         return todoList.objects.all()

class PostList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = todoListSerializer

    def get_queryset(self):
        user = self.request.user
        return todoList.objects.filter(owner=user).order_by('-id')

class PostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer


class CreatePost(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = todoList.objects.all()
    serializer_class = todoListSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = todoListSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(owner=self.request.user)
        articles = todoList.objects.filter(owner=self.request.user)
        serializer = todoListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class EditPost(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = todoListSerializer
    queryset = todoList.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        articles = todoList.objects.filter(owner=self.request.user)
        serializer = todoListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = todoListSerializer
    queryset = todoList.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        articles = todoList.objects.filter(owner=self.request.user)
        serializer = todoListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)