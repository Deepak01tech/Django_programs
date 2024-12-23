from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def wordcount(request):
    data=request.GET['data']
    name=request.GET['full_name']
    dict={}
    words=data.split()
    for ele in words:
        if ele in dict:
            dict[ele]+=1
        else:
            dict[ele]=1
    return render(request,'result.html',{'data':dict,'name':name})