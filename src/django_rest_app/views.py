from django.shortcuts import render
from django.http import JsonResponse
from first_app.models import Student
from django.core.serializers import serialize

# Create your views here.


def home_api(request):
    data = {
        'first_name': 'oscar',
        'last_name': 'thomson',
        'skills': ['python', 'django']
    }
    return JsonResponse(data)


# by for loop + append() method
def student_list_api_1(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()

        student_list = []
        for student in students:
            student_list.append({
                'first_name': student.first_name,
                'last_name': student.last_name,
                'number': student.number
            })

        data = {
            'students': student_list,
            'student_count': student_count
        }
        return JsonResponse(data)


# by serialize() method
def student_list_api_2(request):
    if request.method == 'GET':
        students = Student.objects.all()
        student_count = Student.objects.count()

        student_list = serialize('python', students)

        data = {
            'students': student_list,
            'student_count': student_count
        }
        return JsonResponse(data)
