from django.urls import path, include
from .views import TaskViewSet, index, about, signup, login, logout
from rest_framework.routers import DefaultRouter

# setting routers
router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

# setting app name
app_name = "tasks"

# configuring urls
urlpatterns = [
    path("api/", include(router.urls)),
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]