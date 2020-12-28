from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import parcelListSerializer
from .models import parcelList

# Create your views here.
class ParcelList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = parcelListSerializer

    def get_queryset(self):
        user = self.request.user
        return parcelList.objects.filter(owner=user).order_by('-id')

class ParcelDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = parcelList.objects.all()
    serializer_class = parcelListSerializer


class CreateParcel(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = parcelList.objects.all()
    serializer_class = parcelListSerializer

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = parcelListSerializer(data=data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(owner=self.request.user)
        articles = parcelList.objects.filter(owner=self.request.user).order_by('-id')
        serializer = parcelListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class EditParcel(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = parcelListSerializer
    queryset = parcelList.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        articles = parcelList.objects.filter(owner=self.request.user).order_by('-id')
        serializer = parcelListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class DeleteParcel(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = parcelListSerializer
    queryset = parcelList.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        articles = parcelList.objects.filter(owner=self.request.user).order_by('-id')
        serializer = parcelListSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)