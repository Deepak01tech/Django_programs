from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'normal/index.html')

def signupPage(request):
    return render(request, 'normal/signup.html')