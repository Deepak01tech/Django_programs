from django.urls import path
from . import views
urlpatterns = [
    path('addemp/', views.addemp,name='addemp'),
    path('insertemp/', views.insertEmp,name='insertemp'),
    path('getempdata/', views.getEmpDetails,name='getempdata'),
    path('deleteemp/<int:eid>', views.deleteemp,name='deleteemp'),
    # path('updateemp/<int:eid>', views.deleteemp,name='deleteemp'),
]