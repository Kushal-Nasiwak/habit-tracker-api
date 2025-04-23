**Habit Tracker Project Guide (Django + REST Framework)**

---

### **Overview**
This guide documents the full process of building a Habit Tracker & Productivity API project using Django and Django REST Framework. It's designed to be readable, maintainable, and reusable across future chats and projects.

---

### **Repository**
- GitHub Repo: [https://github.com/Kushal-Nasiwak/habit-tracker-api](https://github.com/Kushal-Nasiwak/habit-tracker-api)

---

### **Project Goals**
- Track user habits and daily productivity.
- Build REST APIs to manage habits, track progress, and review history.
- Use the tool to plan and stay consistent with long-term goals.

---

### **Tech Stack**
- Django (Backend Framework)
- Django REST Framework (API)
- PostgreSQL (Database)
- GitHub (Version Control / Portfolio)

---

### **Steps Completed So Far**

#### **Step 1: Project Setup**
- Created project: `habit_tracker`
- Created app: `tracker`
- Installed dependencies: `djangorestframework`, `psycopg2`, etc.
- Added apps to `INSTALLED_APPS`

#### **Step 2: Models**
- Created `Habit` model with fields:
  ```python
  class Habit(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)
      description = models.TextField(blank=True)
      frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
      created_at = models.DateTimeField(auto_now_add=True)
  ```
- Created `HabitRecord` model:
  ```python
  class HabitRecord(models.Model):
      habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
      date = models.DateField()
      completed = models.BooleanField(default=False)
  ```

#### **Step 3: Serializers**
- Created `HabitSerializer` and `HabitRecordSerializer` to serialize/deserialize model data for API.

#### **Step 4: ViewSets and Routers**
- Used `viewsets.ModelViewSet` for full CRUD access.
- Explained difference between:
  - `ModelViewSet` = Full CRUD
  - `ReadOnlyModelViewSet` = Only `list` and `retrieve`
- Example ViewSet:
  ```python
  class HabitViewSet(viewsets.ModelViewSet):
      queryset = Habit.objects.all()
      serializer_class = HabitSerializer

      def get_queryset(self):
          return self.queryset.filter(user=self.request.user)
  ```
- Registered routers:
  ```python
  router = routers.DefaultRouter()
  router.register(r'habits', HabitViewSet)
  router.register(r'habit-records', HabitRecordViewSet)
  ```

---

### **Coming Up Next: Step 5 - Authentication**
- Use Django REST Framework’s `TokenAuthentication` or `Simple JWT`
- Add login/signup endpoints
- Secure all viewsets using `IsAuthenticated` permission

---

### **How to Use This Document in Future Chats**
Just paste the GitHub file link where this is stored and tell ChatGPT:
> "Here's the context of my Habit Tracker project. Let's continue from Step 5."

ChatGPT will understand and continue right where we left off.

---

### **Your Coding Partner’s Promise**
> “You just bring the will—I’ll bring the way.”

