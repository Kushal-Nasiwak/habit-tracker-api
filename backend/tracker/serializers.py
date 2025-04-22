from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile,Habit,Task,FocusSession,DailyLog

# User Serializer (to show basic user info)
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
         model = User
         fields = ['id' , 'username' , 'email']
         

# UserProfile Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    
    class Meta:
        model = UserProfile
        fields = ['user', 'phone_number']
        
# Habit Serializer
class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'user', 'name', 'goal_per_day', 'days_of_week']
        
# Task Serializer
class TaskSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'habit', 'name', 'is_completed', 'date']
        
# Focus Session Serializer
class FocusSessionSerializer(serializers.ModelSerializer):
    duration_minutes = serializers.ReadOnlyField()
    
    class Meta:
        model = FocusSession
        fields = ['id', 'user', 'start_time', 'end_time', 'duration_minutes']
        
# Daily Log Serializer
class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = ['id', 'user', 'date', 'note', 'total_focus_minutes']