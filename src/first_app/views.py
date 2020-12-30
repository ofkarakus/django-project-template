from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display_home(request):
    return HttpResponse("Home Page")


def display_about(request):
    return HttpResponse("About Page")
