from django.urls import path, include
from .views import TaskViewSet, index, about, signup, login_view, logout_view, task_list, add_task
from rest_framework.routers import DefaultRouter

app_name = "tasks"  # ✅ Ensures namespacing works

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("tasks_list/", task_list, name="task_list"),
    path("", index, name="index"),  
    path("about/", about, name="about"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("add/", add_task, name="add_task"),
]