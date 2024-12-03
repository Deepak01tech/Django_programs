from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view_decorator

# Create your views here.

@api_view_decorator(name='get_data')
def get_data(request):
    data = {
        'message': 'Hello, this is a GET request.'
    }

