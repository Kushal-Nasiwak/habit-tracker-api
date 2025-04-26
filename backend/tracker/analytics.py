from datetime import timedelta, date
from django.db.models import Count, Q
from .models import HabitLog

def get_weekly_habit_summary(user):
    today = date.today()
    week_start = today - timedelta(days = today.weekday()) # Monday
    
    logs = HabitLog.objects.filter(user=user, date_gte=week_start, date_lte=today)
    
    total_logged = logs.count()
    completed_count = logs.filter(completed = True).count()
    
    completion_rate = (completed_count / total_logged) * 100 if total_logged else 0
    
    return{
        "total_logged" : total_logged,
        "completed" : completed_count,
        "completed_rate" : round(completion_rate, 2)
    }
    