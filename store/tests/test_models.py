from rest_framework.test import APITestCase
from store.models import Author, Book

class TestAuthorModel(APITestCase):
    
    def test_create_author(self):
        author = Author.objects.create(first_names='Willian', last_names='Shakeaspeare')
        self.assertIsInstance(author, Author)

    
        

class TestBookModel(APITestCase):
    def setUp(self):
        self.author=Author.objects.create(first_names='Willian', last_names='Shakeaspeare')
        self.author=Author.objects.create(first_names='Tabata', last_names='King')

    def test_create_book(self):
        book = Book.objects.create(title='Hamlet', publication_date='2020-08-01')
        book.authors.set([self.author])
        self.assertIsInstance(book, Book)
