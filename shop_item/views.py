from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets, permissions

from .serializers import ItemSerializer, OrderItemSerializer, OrderSerializer
from .models import Item, OrderItem, Order

from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.
class ItemList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(item_owner=user, ordered=False).order_by('-id')

class ItemDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class CreateItem(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        tracking_no = request.data.get('tracking_no', None)
        item_qs = Item.objects.filter(tracking_no=tracking_no)
       
        if item_qs.exists():
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(item_owner=self.request.user)
        articles = Item.objects.filter(item_owner=self.request.user, ordered=False).order_by('-id')
        serializer = ItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
        

class EditItem(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        articles = Item.objects.filter(item_owner=self.request.user, ordered=False).order_by('-id')
        serializer = ItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class DeleteItem(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        articles = Item.objects.filter(item_owner=self.request.user, ordered=False).order_by('-id')
        serializer = ItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class AddToCartView(APIView):
    def post(self, request, *args, **kwargs):
        tracking_no = request.data.get('tracking_no', None)
        if tracking_no is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)

        item = get_object_or_404(Item, tracking_no=tracking_no)

        order_item = OrderItem.objects.create(
            item=item,
            user=self.request.user,
            ordered=False
        )
        
        order_item.save()

        itemisordered = Item.objects.filter(item_owner=self.request.user, tracking_no=tracking_no)
        itemisordered.update(ordered=True)
        

        articles = Item.objects.filter(item_owner=self.request.user, ordered=False).order_by('-id')
        serializer = ItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class RemoveFromCartView(APIView):
    def post(self, request, *args, **kwargs):
        tracking_no = request.data.get('tracking_no', None)
        if tracking_no is None:
            return Response({"message": "Invalid request"}, status=HTTP_400_BAD_REQUEST)

        itemisordered = Item.objects.filter(item_owner=self.request.user, tracking_no=tracking_no)
        itemisordered.update(ordered=False)  

        articles = Item.objects.filter(item_owner=self.request.user, ordered=True).order_by('-id')
        serializer = ItemSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

class CartList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.request.user
        return Item.objects.filter(item_owner=user, ordered=True).order_by('-id')