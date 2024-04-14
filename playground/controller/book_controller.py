from playground import models
from django.db.models import Q

class book_controller:
    def get_all_books_controller(request):
        try:
            books = models.Book.objects.values('book_id', 'title', 'thumbnail', 'price')

            if not books: return 404, "Books not found!!"

            data = [{'book_id': book['book_id'], 
                     'title': book['title'],
                     'thumbnail': book['thumbnail'],
                     'price': book['price']
                    } for book in books]


            return 201, data
        
        except Exception as e:
            return 500, e
        
    
    def get_books_by_name_controller(request, str_variable):
        try:
            books = models.Book.objects.filter(
                Q(title__icontains=str_variable) | Q(authors__icontains=str_variable)).values('book_id', 'title', 'authors', 'thumbnail', 'price')
        
            if not books: return 404, "Books not found!!"

            data = [{'book_id': book['book_id'], 
                     'title': book['title'],
                     'thumbnail': book['thumbnail'],
                     'authors': book['authors'],
                     'price': book['price']
                    } for book in books]

            return 201, data
        
        except Exception as e:
            return 500, e
        


    def get_book_by_id_controller(request, book_book_id):
        try:
            books_query = models.Book.objects.filter(book_id=book_book_id).values('book_id', 'title', 'authors', 'categories', 'thumbnail', 
                                                         'description', 'published_year', 'average_rating', 'num_pages', 'price')
    
            if books_query.exists():
                book_data = books_query.first() 
            else:
                return 404, "Books not found!!"


            data = {'book_id': book_data['book_id'], 
                    'title': book_data['title'],
                    'authors': book_data['authors'],
                    'categories': book_data['categories'],
                    'thumbnail': book_data['thumbnail'],
                    'description': book_data['description'],
                    'published_year': book_data['published_year'],
                    'average_rating': book_data['average_rating'],
                    'num_pages': book_data['num_pages'],
                    'price': book_data['price']}

            return 201, data
    
        except Exception as e: 
            return 500, e