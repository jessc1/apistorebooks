from django.urls import path
from . import views

urlpatterns = [
    path('store/author/list',views.AuthorListAPIView.as_view(), name='authors'),
    path('store/author/<int:id>', views.AuthorRetrieveAPIView.as_view(), name='author_detail'),
    path('store/books', views.BookListAPIView.as_view(), name='books'),
    path('store/books/<int:id>', views.BookRetrieveAPIView.as_view(), name='book_detail'),
    path('store/books/create', views.BookCreateAPIView.as_view(), name='create_books'),
    path('store/books/update/<int:id>', views.BookUpdateAPIView.as_view(), name='update_book'),
    path('store/books/delete/<int:id>', views.BookDeleteAPIView.as_view(), name='delete_book'),
    ]
