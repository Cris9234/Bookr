from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('book-search/', views.book_search, name='book_search'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('publishers/new/', views.publisher_edit, name='publisher_create'),
    path('books/<book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<pk>/media/', views.book_media, name='book_media')
]
