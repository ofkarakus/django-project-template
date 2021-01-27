from django.urls import path
from . import views

urlpatterns = [
    # function-based
    path('home/', views.home_api),
    path('student-list-1/', views.student_list_api_1),
    path('student-list-2/', views.student_list_api_2),
    path('student-create/', views.student_create_api),
    path('student-delete/', views.student_delete_api),
    path('student-update/', views.student_update_api),
    path('student-list-create/', views.student_list_create_api),
    path('student-details-update-delete/<int:id>/',
         views.student_details_update_delete_api),

    # class-based
    path('student-list-create-cls/', views.StudentListCreate.as_view()),
    path('student-details-update-delete-cls/<int:id>/',
         views.StudentDetailsUpdateDelete.as_view()),

    # class-based-generic
    path('student-list-create-gn/', views.StudentListCreateGn.as_view()),
    path('student-details-update-delete-gn/<int:id>/',
         views.StudentDetailsUpdateDeleteGn.as_view(), name="GetUpdateDelete"),

    # class-based-mixin
    path('student-list-create-mixin/', views.StudentListCreateMixin.as_view()),
    path('student-details-update-delete-mixin/<int:id>/',
         views.StudentDetailsUpdateDeleteMixin.as_view())
]
