import json
from django.core.management.base import BaseCommand
from playground.models import Book

class Command(BaseCommand):
    help = 'Import data from JSON file to database'

    def handle(self, *args, **options):
        try:
            with open('playground/data/books_data.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    Book.objects.create(**item)  
                    
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
