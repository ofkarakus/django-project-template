from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_api),
    path('student-list-1/', views.student_list_api_1),
    path('student-list-2/', views.student_list_api_2),
]
