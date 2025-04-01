from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.filters import OrderingFilter
from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Task viewset API view
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["status", "priority"]
    ordering_fields = ["priority"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @action(detail=True, methods=["post"])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = "Completed"
        task.completed_at = now()
        task.save()
        return Response({"message": "Task marked as completed"}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["post"])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.status = "Pending"
        task.completed_at = None
        task.save()
        return Response({"message": "Task marked as incomplete"}, status=status.HTTP_200_OK)

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
            return redirect("tasks:task_list")
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
            return redirect("tasks:login")
        else:
            # Display form errors to the user
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, "tasks/signup.html", {"form": form})

@api_view(["POST"])
@permission_classes([AllowAny])
def signup_api(request):
    form = CustomUserCreationForm(request.data)
    if form.is_valid():
        user = form.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)