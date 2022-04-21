from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('publishers/', views.publisher_list, name='publisher_list')
]