from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .models import CustomUser

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
    return render(request, "tasks/login.html")

# signup page view
def signup(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if name and email and password1 and password2:
            if password1 == password2:
                CustomUser.objects.create_user(name=name, email=email, password=password1)
                redirect("login")
                print(f"User {CustomUser.name} created successfully!")
            else:
                print("Passwords do not match!")
    else:
        print("Just show the form!")

    return render(request, "tasks/signup.html")