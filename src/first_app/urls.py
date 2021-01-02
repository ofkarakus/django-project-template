from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.display_home_page),
    path('about/', views.display_about_page),
    path('add/', views.display_addstudent_page)
]
