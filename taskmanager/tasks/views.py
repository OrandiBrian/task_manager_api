from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView
from .forms import CustomUserCreationForm
from django.contrib import messages

# Task list view
class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

# Task viewset API view
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# task list view
def task_list(request):
    return render(request, "tasks/task_list.html", {"tasks": Task.objects.all()})

# Index view
def index(request):
    return render(request, "tasks/index.html")

# About page view
def about(request):
    return render(request, "tasks/about.html")

# Login view
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "").strip()
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("tasks:index")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("tasks:login")

    return render(request, "tasks/login.html")

# Logout view
def logout_view(request):
    logout(request)
    return redirect("tasks:login")

# Signup page view
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tasks:index")
    else:
        form = CustomUserCreationForm()
    return render(request, "tasks/signup.html", {"form": form})