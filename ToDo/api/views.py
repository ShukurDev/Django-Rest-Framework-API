from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


# Create your views here.
@api_view(['GET'])
def overView(request):
    api_urls = {
        'List-Task': '/task-list/',
        'Detail-Task': '/task-detail/<int:pk>/',
        'Task-Update': '/task-update/<int:pk>/',
        'Task-Create': '/task-create/',
        'Task-Delete': '/task-delete/<int:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def listview(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailview(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createview(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET, POST'])
def updateview(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
