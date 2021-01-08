from rest_framework import serializers
from .models import Item, OrderItem, Order

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'