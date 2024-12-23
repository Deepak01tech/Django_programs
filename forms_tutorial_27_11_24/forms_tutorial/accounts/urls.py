from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path('signuppage/', views.signupPage,name='signuppage'),
]