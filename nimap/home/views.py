from rest_framework import viewsets
from rest_framework import permissions


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client, Project


from .serializer import ClientSerializer, ProjectSerializer

# Client Viewset
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Project Viewset
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Get projects assigned to the logged-in user
@api_view(['GET'])
def user_projects(request):
    projects = Project.objects.filter(users=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

