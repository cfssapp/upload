from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import basicListSerializer
from .models import basicList

# Create your views here.

@csrf_exempt
def apiOverview(request):
    if request.method == 'POST':
        api_urls = {
            "status": "ok",
            "currentAuthority": "admin",    
        }
        return JsonResponse(api_urls, safe=False)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def basic_list(request):
    """
    List all code articles, or create a new Article.
    """
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


