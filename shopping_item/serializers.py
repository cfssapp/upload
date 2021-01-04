from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = parcelList
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'

