from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signuppage/', views.signupPage, name='signuppage'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
     ]

