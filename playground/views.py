from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from . import models


class BookHandler():
    @api_view(['GET'])
    @staticmethod
    def get_all_book(request):
        try:
            books = models.Book.objects.values('id', 'title', 'cover', 'unit_price')

            if not books:
                return HttpResponse("Error: Books not found!!", status=404)

            data = [{'id': book['id'], 
                     'title': book['title'],
                     'cover': request.build_absolute_uri(f'/api/{book["cover"]}') if book['cover'] else None,
                     'unit_price': book['unit_price']
                    } for book in books]

            return JsonResponse(data, status=201, safe=False)
        
        except Exception as e:
            return HttpResponse(f'Error occur: {e}', status=500)
    

    @api_view(['GET'])
    @staticmethod
    def get_books_by_name(request, str_variable):
        try:
            books = models.Book.objects.filter(title__icontains=str_variable).values('id', 'title', 'cover', 'unit_price')
        
            if not books:
                return HttpResponse("Books not found", status=404)

            data = [{'id': book['id'], 
                     'title': book['title'],
                     'cover': request.build_absolute_uri(f'/api/{book["cover"]}') if book['cover'] else None,
                     'unit_price': book['unit_price']
                    } for book in books]

            return JsonResponse(data, status=200, safe=False)
    
        except Exception as e:
            return HttpResponse(f'Error occur: {e}', status=500)
        


    @api_view(['GET'])
    @staticmethod
    def get_books_by_id(request, book_id):
        try:
            books_query = models.Book.objects.filter(id=book_id).values('id', 'title', 'author', 'category', 'published_year', 
                                                         'summary', 'cover', 'unit_price', 'stock')
    
            if books_query.exists():
                book_data = books_query.first()  # Lấy phần tử đầu tiên của queryset
            else:
                # Xử lý trường hợp không tìm thấy sách
                return HttpResponse("Books not found", status=404)


            data = {'id': book_data['id'], 
                    'title': book_data['title'],
                    'author': book_data['author'],
                    'category': book_data['category'],
                    'published_year': book_data['published_year'],
                    'summary': book_data['summary'],
                    'cover': request.build_absolute_uri(f'/api/{book_data["cover"]}') if book_data['cover'] else None,
                    'unit_price': book_data['unit_price'],
                    'stock': book_data['stock']}

            return JsonResponse(data, status=200, safe=False)
    
        except Exception as e:
            return HttpResponse(f'Error occur: {e}', status=500)


