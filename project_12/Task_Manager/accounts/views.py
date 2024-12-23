from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializer import UserSerializer
# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":500, "message":"something went wrong","error":serializer.errors})
        serializer.save()
        return Response({"status":200, "message":"User created successfully"})
