from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import *
from api.serializers import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'api overview' : '',
		'create' : '/task-create/',
		'list' : '/task-list/',
		'detail view' : '/task-list/<int:pk>',
		'update' : '/task-update/<int:pk>',
		'delete' : '/task-delete/<int:pk>',
	}

	return Response(api_urls)

@api_view(['GET'])
def showAllTasks(request):
	tasks = todo.objects.all()
	serializer = todoSerializer(tasks, many = True)
	return Response(serializer.data)

@api_view(['GET'])
def showTask(request, pk):
	tasks = todo.objects.get(pk=pk)
	serializer = todoSerializer(tasks, many = False)
	return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
	serializer = todoSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def updateTask(request, pk):
	task = todo.objects.get(pk=pk)
	serializer = todoSerializer(instance = task, data = request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)	

@api_view(['DELETE'])
def deleteTask(request, pk):
	task = todo.objects.get(pk=pk)
	task.delete()
	
	return Response('Item deleted succesfully!')

