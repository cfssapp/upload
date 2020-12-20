from rest_framework import serializers
from .models import basicList

class basicListSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = basicList
        # fields = ['id', 'title', 'author']
        fields ='__all__'

