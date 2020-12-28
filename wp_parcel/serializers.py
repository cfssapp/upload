from rest_framework import serializers
from .models import todoList

class parcelListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = todoList
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'

