from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from first_app.models import Student
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status

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

        # VALIDATION SHOULD BE ADDED FOR POST DATA

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


@csrf_exempt
def student_update_api(request):
    if request.method == 'POST':
        post_body = json.loads(request.body)  # convert json to dict

        student_id = post_body.get('id')
        name = post_body.get('first_name')
        surname = post_body.get('last_name')
        number = post_body.get('number')

        student_data = {
            'first_name': name,
            'last_name': surname,
            'number': number
        }

        # VALIDATION SHOULD BE ADDED FOR POST DATA

        student_obj = Student.objects.filter(id=student_id)

        data = {'success': {
            'message': f'Student updated successfully.'
        }, 'error': {
            'message': f'Student couldn\'t find.'
        }}

        if student_obj.exists():
            student_obj.update(**student_data)

            return JsonResponse(data['success'], status=200)
        return JsonResponse(data['error'], status=200)


@api_view(["GET", "POST"])
def student_list_create_api(request):

    # DISPLAY STUDENT LIST
    if request.method == "GET":
        student_list = Student.objects.all()
        serializer = StudentSerializer(
            student_list, many=True)  # convert dict to json
        return Response(serializer.data)

    # CREATE NEW STUDENT
    elif request.method == "POST":
        serializer = StudentSerializer(
            data=request.data)  # convert json to dict
        if serializer.is_valid():
            
            # If user (teacher) authentication exists in the project;
            # serializer.save(teacher=request.user)
            # Before saving to DB you can assign and send every kind of data by this method.
            
            # This code block is equal to ==>
            # student = form.save(commit=False)
            # student.teacher = request.user
            # student.save()
            
            # There is not user authentication in the project, so that;
            serializer.save()  # this code block is enough for now.
            message = {
                'success': 'Student created successfully!'
            }
            return Response(message, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def student_details_update_delete_api(request, id):
    student = get_object_or_404(Student, id=id)
    print(student)
    print(type(student))
    messages = {'success': {
        'update': 'Student updated succesfully!',
        'delete': 'Student deleted succesfully!'
    }}

    # DISPLAY STUDENT DETAILS
    if request.method == "GET":
        serializer = StudentSerializer(student)  # convert dict to json
        return Response(serializer.data)

    # UPDATE STUDENT DETAILS
    if request.method == "PUT":
        serializer = StudentSerializer(
            student, data=request.data)  # convert json to dict
        if serializer.is_valid():
            serializer.save()
            return Response(messages['success']['update'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE STUDENT
    if request.method == "DELETE":
        student.delete()
        return Response(messages['success']['delete'], status=status.HTTP_200_OK)
