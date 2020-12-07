from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer, ArticleSerializer, basicListSerializer

from .models import Task, Article, basicList
# Create your views here.



@csrf_exempt
@api_view(['GET'])
def apiOverview(request):
	api_urls = [{
        "logo": "https://64.media.tumblr.com/avatar_84bf27cec37f_128.pnj",
        "title": "Albert Einstein",
        "href": "https://www.google.com.my/",
        "subDescription": "Imagination is more important than knowledge",
        
        "owner": "User",
        "createdAt": 1607155074056,
        "updatedAt": 1607155074056,
        "percent": 83,
        "status": "active", 
    }]
    todo_urls = [{
    "code": 0,
    "message": "操作成功",
    "body": [
        {
            "id": 8,
            "title": "完成Antd-Pro-Generator手动添加接口并生成代码",
            "status": 0
        },
        {
            "id": 7,
            "title": "修改Antd-Pro-Generator UI",
            "status": 0
        },
        {
            "id": 6,
            "title": "完善Antd-Pro-Generator数据类型定义",
            "status": 0
        },
        {
            "id": 5,
            "title": "文章使用Antd-Pro-Generator生成代码",
            "status": 1
        },
        {
            "id": 4,
            "title": "Antd-Pro-Generator支持TypeScript",
            "status": 2
        },
        {
            "id": 3,
            "title": "发布Antd-Pro-Generator vscode 插件",
            "status": 1
        },
        {
            "id": 2,
            "title": "文章Ant Design Pro 快速入门",
            "status": 1
        },
        {
            "id": 1,
            "title": "文章React快速入门",
            "status": 1
        }
    ]
}]
	return JsonResponse(todo_urls, safe=False)

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

@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)


@csrf_exempt
def basic_list(request):
    """
    List all code basicLists, or create a new Article.
    """
    if request.method == 'GET':
        basicLists = basicList.objects.all()
        serializer = basicListSerializer(basicLists, many=True)
        return JsonResponse(serializer.data, safe=False)



    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = basicListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)