from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from first_app.models import Student
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json

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


@csrf_exempt
def student_create_api(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)  # convert json to dict

        print(post_body)
        print(type(post_body))

        name = post_body.get('first_name')
        surname = post_body.get('last_name')
        number = post_body.get('number')

        student_data = {
            'first_name': name,
            'last_name': surname,
            'number': number
        }

        student_obj = Student.objects.create(**student_data)
        data = {
            'message': f'Student {student_obj.first_name} created successfully.'
        }
        return JsonResponse(data, status=201)


@csrf_exempt
def student_delete_api(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)  # convert json to dict
        student_id = post_body.get('id')
        student_obj = get_object_or_404(Student, id=student_id)
        student_obj.delete()
        data = {
            'message': f'Student {student_obj.first_name} deleted successfully.'
        }
        return JsonResponse(data, status=201)
