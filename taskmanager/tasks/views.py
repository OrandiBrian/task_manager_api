from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Task list view
class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

# Task viewset API view
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# task list
@login_required
def task_list(request):
    tasks = Task.objects.filter(user = request.user)
    return render(request, "tasks/task_list.html", {
        "tasks": tasks
    })

# create tasks
@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        priority = request.POST.get("priority", "")
        status = request.POST.get("status", "")

        if title:
            Task.objects.create(title=title, description=description, priority=priority, status=status, user=request.user)
            return redirect("tasks:task_list")

    return render(request, "tasks/add.html")

@login_required
def task_detail(request, pk):
    task = Task.objects.filter(user = request.user).get(pk=pk)
    return render(request, "tasks/task.html", {
        "task": task
    })

# edit task
@login_required
def edit_task(request, pk):
    task = Task.objects.filter(user = request.user).get(pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        priority = request.POST.get("priority", "")
        status = request.POST.get("status", "")

        if title:
            task.title = title
            task.description = description
            task.priority = priority
            task.status = status
            task.save()

            return redirect("tasks:task_list")      
    
    return render(request, "tasks/edit.html", {
        "task": task
    })

# delete task
@login_required
def delete_task(request, pk):
    task = Task.objects.filter(user = request.user).get(pk=pk)
    task.delete()
    return redirect("tasks:task_list")

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