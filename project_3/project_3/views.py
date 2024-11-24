from django.shortcuts import render

def about(request):
    return render(request, 'index.html')

def result(request):
    data=request.GET['data']
    dict={}
    for i in data.split(' '):
        if ele in dict:
            dict[ele]+=1
        else:
            dict[ele]=1

    return render(request, 'result.html',dict)





