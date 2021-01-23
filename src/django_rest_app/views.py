from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home_api(request):
     data = {
         'first_name': 'oscar',
         'last_name': 'thomson',
         'skills': ['python', 'django']
     }
     return JsonResponse(data)