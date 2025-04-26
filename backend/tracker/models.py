from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=15 , blank=True , null=True)
    
    def __str__(self):
        return self.user.username
    
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    goal_per_day = models.IntegerField(default=1)
    days_of_week = models.CharField(max_length=100 , help_text = "Comma-separated days: Mon,Tue,Wed...")
    
    def __str__(self):
        return f"{self.name} - {self.user.username}"
    
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit , on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    data =  models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class FocusSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField
    
    @property
    def duration_minutes(self):
        return (self.end_time - self.start_time).seconds // 60
    
    def __str__(self):
        return f"{self.user.username} - {self.duration_minutes} min"
    
class DailyLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)
    total_focus_minutes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"
    

class HabitLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ['user', 'habit', 'date']  # ✅ Prevent duplicate check-ins
        
    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'✅' if self.completed else '❌'}"