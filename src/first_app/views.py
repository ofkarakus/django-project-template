from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def display_home(request):
    # print(request.GET.get("q"))
    # print(request.COOKIES)
    # print(request.user)
    # print(request.path)
    # print(request.method)
    my_context = {
        'title': '<b>clarusway</b>',
        'dict_1': {'django': 'best framework'},
        'my_list': [2, 3, 4, 5]
    }
    return render(request, 'first_app/home.html', my_context)


def display_about(request):
    return HttpResponse("About Page")
