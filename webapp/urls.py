from django.contrib import admin
from django.urls import path, include
from .views import get_post, single_data

urlpatterns = [
    path('getpost/', get_post, name='getpost'),
    path('single/<Emp_ID>', single_data, name='singledata'),
]
