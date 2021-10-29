
import pandas as pd

#from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from store.models import Author

class Command(BaseCommand):
    help = 'Load the reviews data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('--csv', type=str)

    def handle(self, *args, **options):
        df = pd.read_csv('authors.csv')
        for first_names, last_names in zip(df.first_name, df.last_name):
            models=Author(first_names=first_names, last_names=last_names)
            models.save()
            
