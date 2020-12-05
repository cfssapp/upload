from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ArticleSerializer

from .models import Task, Article
# Create your views here.



@csrf_exempt
@api_view(['GET'])
def apiOverview(request):
	api_urls = [{
        "id": "fake-list-0",

        "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
        "title": "Alipay",
        "href": "https://ant.design",
        "subDescription": "那是一种内在的东西， 他们到达不了，也无法触及的",
        
        "owner": "付小小",
        "createdAt": 1607155074056,
        "updatedAt": 1607155074056,
        "percent": 83,
        "status": "active", 
    }]
	return JsonResponse(api_urls, safe=False)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')



@csrf_exempt
def article_list(request):
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
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)