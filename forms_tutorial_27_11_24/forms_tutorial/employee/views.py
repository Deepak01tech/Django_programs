from django.shortcuts import render,redirect
from .forms import EmpForm
from .models import Employee
# Create your views here.

def addemp(request):
    empform = EmpForm()
    return render(request,'addemp.html',{'empform':empform})


def getEmpDetails(request):
    employees = Employee.objects.all()
    return render(request,'empdetails.html',{'employees':employees})


def insertEmp(request):
    if request.method == "POST":
        empForm = EmpForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            return redirect('getempdata')
    #     else:
    #         return redirect('addemp')
    # else:
    #     return redirect('addemp')


def deleteemp(request,eid):
    emp = Employee.objects.get(eid=eid)
    emp.delete()
    return redirect('getempdata')

def editEmp(request,eid):
    emp = Employee.objects.get(eid=eid)
    return render(request,'editemp.html',{'emp':emp})


def updateEmp(rquest,eid):
    if rquest.method == "POST":
        emp = Employee.objects.get(eid=eid)
        form = EmpForm(rquest.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('getempdata')