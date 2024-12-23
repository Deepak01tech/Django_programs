from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializer import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all tasks for the logged-in user and creating a new task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the created task
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, or deleting a specific task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Return only tasks belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)
