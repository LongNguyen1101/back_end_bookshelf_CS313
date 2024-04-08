from playground import models

class book_controller:
    def get_all_books_controller(request):
        try:
            books = models.Book.objects.values('id', 'title', 'cover', 'unit_price', 'product_type')

            if not books: return 404, "Books not found!!"

            data = [{'id': book['id'], 
                     'title': book['title'],
                     'cover': request.build_absolute_uri(f'/api/{book["cover"]}') if book['cover'] else None,
                     'unit_price': book['unit_price'],
                     'product_type': book['product_type']
                    } for book in books]


            return data, None
        
        except Exception as e:
            return 500, e
        
    
    def get_books_by_name_controller(request, str_variable):
        try:
            books = models.Book.objects.filter(title__icontains=str_variable).values('id', 'title', 'cover', 'unit_price', 'product_type')
        
            if not books: return 404, "Books not found!!"

            data = [{'id': book['id'], 
                     'title': book['title'],
                     'cover': request.build_absolute_uri(f'/api/{book["cover"]}') if book['cover'] else None,
                     'unit_price': book['unit_price'],
                     'product_type': book['product_type']
                    } for book in books]

            return data, None
        
        except Exception as e:
            return 500, e
        


    def get_book_by_id_controller(request, book_id):
        try:
            books_query = models.Book.objects.filter(id=book_id).values('id', 'title', 'author', 'category', 'published_year', 
                                                         'summary', 'cover', 'unit_price', 'stock', 'product_type')
    
            if books_query.exists():
                book_data = books_query.first()  # Lấy phần tử đầu tiên của queryset
            else:
                # Xử lý trường hợp không tìm thấy sách
                return 404, "Books not found!!"


            data = {'id': book_data['id'], 
                    'title': book_data['title'],
                    'author': book_data['author'],
                    'category': book_data['category'],
                    'published_year': book_data['published_year'],
                    'summary': book_data['summary'],
                    'cover': request.build_absolute_uri(f'/api/{book_data["cover"]}') if book_data['cover'] else None,
                    'unit_price': book_data['unit_price'],
                    'stock': book_data['stock'],
                    'product_type': book_data['product_type']}

            return data, None
    
        except Exception as e: 
            return 500, e