from django.shortcuts import render
import mysql.connector as sql
#global variables for five enteries

em=''
pwd=''

# Create your views here.
def login(request):
    global em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="deepak",database="nimap")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():

            if key=='email':
                em=value
            elif key=='password':
                pwd=value

        c="select * from  users where email ='{}' and password ='{}'" .format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t == ():
            return render(request,'error.html')
        else:
            return render(request,'home.html')

    return render(request,'login.html')

