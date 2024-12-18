
from django.contrib import admin
from django.urls import path,include
from .views import  *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # path('student/',StudentAPI.as_view()),
    path('register/',RegisterAPI.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('student-generic/', StudentGeneric.as_view()),
    path('student-generic-update/<id>/', StudentGeneric1.as_view()),
    # path('getall-students',home),
    # path('register-student',register_student),
    # path('update-student/<id>',update_student),
    # path('delete-student/<id>',delete_student),
]