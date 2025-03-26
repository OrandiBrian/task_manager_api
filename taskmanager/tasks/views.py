from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# Task viewset API view
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# index view
def index(request):
    return render(request, "tasks/index.html")

# about page view
def about(request):
    return render(request, "tasks/about.html")