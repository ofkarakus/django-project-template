from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_api),
    path('student-list-1/', views.student_list_api_1),
    path('student-list-2/', views.student_list_api_2),
    path('student-create/', views.student_create_api),
    path('student-delete/', views.student_delete_api),
    path('student-update/', views.student_update_api),
    path('student-list-create/', views.student_list_create_api),
    path('student-details-update-delete/<int:id>/',
         views.student_details_update_delete_api),
    path('student-list-create-cls/', views.StudentListCreate.as_view()),
    path('student_details_update_delete-cls/<int:id>/',
         views.StudentDetailsUpdateDelete.as_view()),
]
