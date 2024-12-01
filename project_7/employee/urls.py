from django.urls import path
from . import views

urlpatterns = [
    path('addemp', views.addemp, name='addemp'),
    path('insertemp', views.insertemp, name='insertemp'),
    path('getempdata', views.getempdata, name='getempdata'),
    path('editempdata', views.editempdata, name='editempdata'),
    path('deleteemp/<int:eid>', views.deleteemp, name='deleteemp'),
    path('updateemp/<int:eid>', views.updateemp, name='updateemp'),


    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]
