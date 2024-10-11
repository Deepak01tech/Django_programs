from django.shortcuts import render
import mysql.connector as sql
#global variables for five enteries
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def regsiter(request):
    global fn,ln,s,em,pwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user="root",passwd="deepak",database="nimap")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='first_name':
                fn=value
            elif key=='last_name':
                ln=value
            elif key=='sex':
                s=value
            elif key=='email':
                em=value
            elif key=='password':
                pwd=value

        c="insert into users Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        m.commit()
    return render(request,'register.html')

