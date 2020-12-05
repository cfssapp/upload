from rest_framework import serializers
from .models import Task, Article, basicList


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author']
        fields ='__all__'

class basicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = basicList
        fields ='__all__'