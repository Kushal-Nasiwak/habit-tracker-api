from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HabitViewSet, TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'habits',HabitViewSet,basename='habit')
router.register(r'tasks',TaskViewSet,basename='task')
router.register(r'users',UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]