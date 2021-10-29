from django.db import models

class Author(models.Model):
    """
    A contributor to a Book
    """
    first_names = models.CharField\
                  (max_length=50,\
                   null = False, \
                   help_text=\
                   "The contributor's first name or names")
    last_names = models.CharField\
                 (max_length=50,\
                  null = False, \
                  help_text=\
                  "The contributor's last name or names")
    

    def __str__(self):
        return self.first_names


class Book(models.Model):
    """ A published book."""
    title = models.CharField \
            (max_length = 70, 
             help_text="The title of the book")
    publication_date = models.DateField \
                       (verbose_name =\
                        "Date the book was published.")
   
    
    authors = models.ManyToManyField \
                   ('Author')

    def __str__(self):
        return self.title    

