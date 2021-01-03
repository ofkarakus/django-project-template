from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.display_home_page, name='Home Page'),
    path('about/', views.display_about_page, name='About Page'),
    path('form/', views.display_form, name='Form Page'),
    path('list/', views.get_student_list, name='List Page'),
    path('add/', views.add_student, name='Add Page'),
    path('<int:id>/detail/', views.get_student_details, name='Detail Page'),
    path('<int:id>/delete/', views.delete_student, name='Delete Student')
]
