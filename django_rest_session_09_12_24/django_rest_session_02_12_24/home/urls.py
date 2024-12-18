
from django.contrib import admin
from django.urls import path,include
from .views import  *



urlpatterns = [
    path('student/',StudentAPI.as_view())
    # path('getall-students',home),
    # path('register-student',register_student),
    # path('update-student/<id>',update_student),
    # path('delete-student/<id>',delete_student),
]