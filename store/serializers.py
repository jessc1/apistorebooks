from rest_framework import serializers
from .models import Author, Book


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'first_names',
            'last_names',
            
        ]

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'first_names',
            'last_names',
            
        ]
    
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'publication_date',
            'authors',            
            ]


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'publication_date',
            'authors',            
            ]



