from django.urls import path

from .views import BookRecordFormView, FormSuccessView, BookCreateView, BookUpdateView, BookDeleteView, FormDeleteView
from .views import BookReadDetailView

urlpatterns = [
    path('book_record_detail/<int:pk>', BookReadDetailView.as_view(), name='book_detail'),
    path('book_record_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('book_record_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
    path('book_record_create', BookCreateView.as_view(), name='book_create'),
    path('new_book_record', BookRecordFormView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('delete_success', FormDeleteView.as_view(), name='form_delete'),
]
