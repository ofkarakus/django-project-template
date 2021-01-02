from django.shortcuts import render
from django.http import HttpResponse

from first_app.forms import StudentForm

# Create your views here.


def display_home_page(request):
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


def display_about_page(request):
    return HttpResponse("About Page")


def display_addstudent_page(request):
    form = StudentForm()
    html = 'Welcome'
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            html = 'Student successfully added'

    context = {
        'form': form,
        'html': html
    }
    return render(request, 'first_app/student_add.html', context)
