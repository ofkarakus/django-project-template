from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from first_app.models import Student
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


def display_form(request):
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
    return render(request, 'first_app/form.html', context)


def get_student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'first_app/student_list.html', context)


def add_student(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("List Page")
    context = {
        'form': form,
    }
    return render(request, 'first_app/add_student.html', context)


def get_student_details(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'first_app/student_detail.html', context)


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('List Page')
    return render(request, 'first_app/delete_student.html')
