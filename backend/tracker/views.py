# from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserProfile, Habit, Task, FocusSession, DailyLog
from .serializers import (
    UserSerializer,
    UserProfileSerializer,
    HabitSerializer,
    TaskSerilazer,
    FocusSessionSerializer,
    DailyLogSerializer
)

# Create your views here.

# User ViewSet (Read-only)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
#  User Profile ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
# Habit Viewset
class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
# Task ViewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerilazer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
# Focus Session Viewset
class FocusSessionViewSet(viewsets.ModelViewSet):
    queryset = FocusSession.objects.all()
    serializer_class = FocusSessionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
# Daily Log ViewSet
class DailyLogViewSet(viewsets.ModelViewSet):
    queryset = DailyLog
    serializer_class = DailyLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)