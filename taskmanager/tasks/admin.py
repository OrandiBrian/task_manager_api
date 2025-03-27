from django.contrib import admin
from .models import Task, CustomUser
from django.contrib.auth.admin import UserAdmin

class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "priority", "status", "completed_at"]
    search_fields = ["title", "priority"]
    list_filter = ["priority", "status"]

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_active", "is_superuser", "is_staff", "date_joined", "last_login"]
    search_fields = ["name", "email"]

# register sites
admin.site.register(Task, TaskAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser, UserAdmin)