from django.contrib.auth.models import User
from django.db import models

# creating Task model
class Task(models.Model):
    # priority choices
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    # status choices
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    ]

    # model attributes
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="Pending")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    completed_at = models.DateTimeField(null=True, blank=True)

    # string representation of the model
    def __str__(self):
        return self.title
