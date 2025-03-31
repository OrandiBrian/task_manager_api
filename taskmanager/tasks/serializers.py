from rest_framework import serializers
from .models import Task

# creating task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "priority", "status", "completed_at", "user"]
        read_only_fields = ["user", "completed_at"]