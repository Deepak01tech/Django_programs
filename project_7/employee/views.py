from django.shortcuts import render, redirect
from .forms import EmpForm
from .models import Employee

def addemp(request):
    empform = EmpForm()
    return render(request, 'addemp.html', {'empform':empform})

def getEmpDetails(request):
    employees = Employee.objects.all()
    return render(request, 'empdetails.html', {'employees':employees})

def insertEmp(request):
    if request.method == 'POST':
        empform = EmpForm(request.POST)
        if empform.is_valid():
            empform.save()
            return redirect('getEmpDetails')

def deleteemp(request, eid):
    employee = Employee.objects.get(eid=eid)
    employee.delete()
    return redirect('getEmpDetails')

def editemp(request, eid):
    employee = Employee.objects.get(eid=eid)
    empform = EmpForm(instance=employee)
    return render(request, 'editemp.html', {'empform':empform})

def updateemp(request, eid):
    if request.method == 'POST':
        employee = Employee.objects.get(eid=eid)
        empform = EmpForm(request.POST, instance=employee)
        if empform.is_valid():
            empform.save()
            return redirect('getEmpDetails')


# Create your views here.
