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
            print("testt")
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
