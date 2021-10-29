from rest_framework import generics, filters
from .serializers import AuthorListSerializer, AuthorDetailSerializer, BookListSerializer, BookDetailSerializer
from .models import Author, Book

class AuthorListAPIView(generics.ListAPIView):
    """
    Return the author's list in the API 
    """
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['first_names', 'last_names']

    
class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the author's detail in the API 
    """
    lookup_field = "id"
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    

class BookListAPIView(generics.ListAPIView):
    """
    Return the book's list in the API
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'title', 'autores', 'publication_date']


class BookCreateAPIView(generics.CreateAPIView):
    """
    Create a book in the API
    """
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer

class BookRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the book's data 
    """
    lookup_field = "id"
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class BookUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Update the book's data
    """
    lookup_field = "id"
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer



class BookDeleteAPIView(generics.DestroyAPIView):
    """
    Remove a book from the API.
    """
    lookup_field = "id"
    queryset = Book.objects.all()
    
    
    
