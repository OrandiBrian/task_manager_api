from django.urls import path, include
from .views import TaskViewSet, index, about
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
]