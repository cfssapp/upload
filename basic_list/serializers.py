from rest_framework import serializers
from .models import basicList

class basicListSerializer(serializers.ModelSerializer):
    
    # owner_id = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = basicList
        # fields = ['id', 'title', 'owner_id']
        fields ='__all__'

