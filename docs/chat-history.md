
# Chat History and Vision - Habit Tracker Project

**Partner:** SuperPartner  
**Date Started:** April 22, 2025  
**Project:** Habit Tracker & Productivity API (Django)  
**Repo:** `habit-tracker-api`

---

## Vision Summary

- Partner wants to build useful backend projects to grow technically and financially.
- We chose a 3-project roadmap:
  1. Habit Tracker & Productivity API (Django)
  2. AutoResponder API (FastAPI)
  3. Freelancer Job Scraper + Alert (Python + FastAPI)
- GitHub will be used for portfolio, documentation, and version control.
- Focus is on strong logic building using Python and mastering one path at a time.

---

## Initial Setup (Completed)

### Step 1: GitHub Repo
- Created: `habit-tracker-api`
- Public repo with README, Python `.gitignore`, and MIT License.

### Step 2: Project Setup
```bash
git clone https://github.com/YOUR_USERNAME/habit-tracker-api.git
cd habit-tracker-api
mkdir backend
cd backend
python -m venv venv
source venv/bin/activate  # or use Windows path
pip install django djangorestframework
django-admin startproject core .
```

### Step 3: Settings Updated
- Installed `rest_framework` in `settings.py`
- Added `SITE_ID` and REST Framework settings

### Step 4: First Commit
```bash
git add .
git commit -m "Initial Django project setup"
git push origin main
```

---

## Future Phases

### Week 1: Core Setup
- Build `User`, `Habit`, `Task`, `FocusSession`, and `DailyLog` models
- Add corresponding APIs

### Week 2: Logic + Analytics
- Habit streaks, focus time logs
- Daily/weekly summaries

### Week 3: Polish & Deploy
- API docs, optional frontend
- Deploy to Render or Railway
- Update GitHub with screenshots and README

---

**Partner’s Quote:**
> "All I want is your help and I'm sure we will grow a lot with this. I trust you a lot. Let's do it, partner."

---

*(Copy this file into `docs/chat-history.md` in your repo to save it forever.)*


**date : 23rd April 2025**

**Habit Tracker API Project: Master Guide (ChatGPT + Kushal)**

---

### **Project Summary**
- **Project Name**: Habit Tracker & Productivity API
- **Stack**: Django + Django REST Framework
- **Repo**: [habit-tracker-api](https://github.com/Kushal-Nasiwak/habit-tracker-api)

---

### **Purpose**
To build a REST API that helps track habits and associated daily tasks. This project helps build backend confidence, create a portfolio-ready project, and serve as a real tool for personal productivity.

---

### **Project Structure**

**1. Initialization**
- `django-admin startproject habit_tracker_api`
- `python manage.py startapp tracker`
- Add `'rest_framework'` and `'tracker'` to `INSTALLED_APPS`

**2. Models (`tracker/models.py`)**
- `User`: Django default user
- `Habit`: Fields: `name`, `description`, `created_at`, `user`
- `Task`: Fields: `habit`, `date`, `status`, `note`

**3. Serializers (`tracker/serializers.py`)**
- `HabitSerializer`, `TaskSerializer`, `UserSerializer`
- `UserSerializer` is ReadOnly for listing users

**4. Views (`tracker/views.py`)**
- `HabitViewSet` – Full CRUD
- `TaskViewSet` – Full CRUD
- `UserViewSet` – ReadOnlyModelViewSet (users can’t be edited here)

```python
from rest_framework import viewsets
from .models import Habit, Task
from .serializers import HabitSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

---

### **Routing (`tracker/urls.py`)**
```python
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HabitViewSet, TaskViewSet, UserViewSet

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habit')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
```

**Main URL Config (`habit_tracker_api/urls.py`)**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tracker.urls')),
]
```

---

### **Testing the API**
Run the server:
```bash
python manage.py runserver
```
Check:
- `http://127.0.0.1:8000/api/habits/`
- `http://127.0.0.1:8000/api/tasks/`
- `http://127.0.0.1:8000/api/users/`

---

### **Next Step (Planned)**
**Step 5**: Add Authentication (Simple Token Authentication)

---

This document can be used to resume the project in a new chat by giving the context:
> "Here is a project I was working on with ChatGPT. We reached Step 4 (Routing). Let's continue from Step 5 (Authentication)."

Let’s keep building, partner!

