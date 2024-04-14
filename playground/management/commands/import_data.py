import json
from django.core.management.base import BaseCommand
from playground import models
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Import data from JSON file to database'

    def handle(self, *args, **options):
        try:
            with open('playground/data/books_data.json', 'r') as file:
                data = json.load(file)
                for item in data:
                    models.Book.objects.create(**item)  
                    
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

        try:
            with open('playground/data/transactions.json', 'r') as file:
                transactions = json.load(file)

                for i in range(len(data)):
                    order, _ = models.PurchaseOrder.objects.get_or_create()
                    price = 0

                    for item in data[i]['items']:
                        book_id = item['book_id']
                        quantity = item['quantity']

                        book = get_object_or_404(models.Book, book_id=book_id)
                        order_item, _ = models.OrderDetail.objects.get_or_create(order=order, book=book)
                        order_item.quantity = quantity
                        price += book.price * quantity
                        order_item.save()

                    order.total = round(price, 2)
                    order.save()
                    
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))

        
