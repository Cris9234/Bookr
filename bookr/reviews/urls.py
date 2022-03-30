from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome_view'), # non ho capito a che serve dargli un nome...
]