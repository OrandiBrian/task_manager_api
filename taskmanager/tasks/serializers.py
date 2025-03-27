from rest_framework import serializers
from .models import Task

# creating task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["user", "created_at"]