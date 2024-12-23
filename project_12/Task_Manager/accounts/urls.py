from django.contrib import admin
from django.urls import  path,include
from .views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,


)
urlpatterns = [
    path('', RegisterAPI.as_view()),
    path('login/', TokenObtainPairView.as_view(),name ='token_obtain_pair'),
]
