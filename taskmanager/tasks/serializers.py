from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task

# creating task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"