from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

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

# login page view
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "tasks/login.html")

# logout page view
def logout(request):
    logout(request)
    return redirect("login")

# signup page view
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "tasks/signup.html", {"form": form})