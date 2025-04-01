from django.urls import path, include
from .views import TaskViewSet, signup_api, index, about, signup, login_view, logout_view, task_list, add_task, task_detail, edit_task, delete_task
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "tasks"

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = [
    path("api/", include(router.urls)),
    path("signup_api/", signup_api, name="sign_up"), # signup view for API
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("tasks_list/", task_list, name="task_list"),
    path("", index, name="index"),  
    path("about/", about, name="about"),
    path("signup/", signup, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("add/", add_task, name="add_task"),
    path("tasks_list/<int:pk>/", task_detail, name="task"),
    path("tasks_list/<int:pk>/edit/", edit_task, name="edit_task"),
    path("tasks_list/<int:pk>/delete/", delete_task, name="delete_task"),
]