from rest_framework.test import APITestCase
from django.urls import reverse
from django.test import Client
from store.models import Author, Book


class TestAuthorView(APITestCase):

    
    def test_author_list_view(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)


class TestBookView(APITestCase):
    def test_book_create_view(self):
        response =self.client.post(reverse('create_books'), {
            'title':'Hamlet',
            'publication_date':'2020-08-01',
            'authors': ['8','7']
            
        })

    def test_book_list_view(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        
     
    def test_book_update_view(self): 
        response = self.client.put(reverse('update_book', args='1'), {
            'title':'Dune',
            'publication_data' :'1990-012-20',
            'authors': ['3','4'],            
            
        })


    def test_book_delete_view(self): 
        response = self.client.delete(
            reverse('delete_book', args='1'))

