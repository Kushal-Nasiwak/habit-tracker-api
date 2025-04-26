from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HabitViewSet, TaskViewSet, UserViewSet, HabitLogViewSet, FocusSessionViewSet, UserProfileViewSet, DailyLogViewSet 

router = DefaultRouter()
router.register(r'habits',HabitViewSet,basename='habit')
router.register(r'tasks',TaskViewSet,basename='task')
router.register(r'users',UserViewSet, basename='user')
router.register(r'focus-sessions', FocusSessionViewSet, basename='focussession')
router.register(r'daily-logs', DailyLogViewSet, basename='dailylog')
router.register(r'user-profiles', UserProfileViewSet, basename='userprofile')
router.register(r"habit-logs",HabitLogViewSet,basename='hanbitlog')


urlpatterns = [
    path('', include(router.urls)),
]