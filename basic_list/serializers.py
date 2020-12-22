from rest_framework import serializers
from .models import todoList

class basicListSerializer(serializers.ModelSerializer):
    
    # owner_id = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = todoList
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'

