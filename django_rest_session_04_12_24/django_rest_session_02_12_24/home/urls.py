
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('getall-students',views.home),
    path('register-student',views.register_student),
    path('update-student/<id>',views.update_student),
    path('delete-student/<id>',views.delete_student),
]