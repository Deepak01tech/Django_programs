from django.urls import path
from . import views
urlpatterns = [
    path('addemp/', views.addemp,name='addemp'),
    path('insertemp/', views.insertEmp,name='insertemp'),
    path('getempdata/', views.getEmpDetails,name='getempdata'),
    path('editEmp/<int:eid>',views.editEmp,name="editEmp"),
    path('updateEmp/<int:eid>',views.updateEmp,name="updateEmp"),
    path('deleteemp/<int:eid>', views.deleteemp,name='deleteemp'),
    # path('updateemp/<int:eid>', views.deleteemp,name='deleteemp'),
]