from django.urls import path
from .views import display_about, display_home

urlpatterns = [
    path('home/', display_home),
    path('about/', display_about)
]
