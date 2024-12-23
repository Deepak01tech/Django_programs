from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    # API endpoints for tasks
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
