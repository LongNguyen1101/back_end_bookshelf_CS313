from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from playground.controller.book_controller import book_controller
from playground.controller.order_controller import order_controller


class api_handler:
    # api/books/
    @api_view(['GET'])
    @staticmethod
    def get_all_books(request):
        status_code, msg = book_controller.get_all_books_controller(request)

        if status_code == 201: 
            return JsonResponse(msg, status=201, safe=False)
        else:
            return HttpResponse(f"Error: {msg}", status=status_code)
        
    

    # api/books/{str_variable}
    @api_view(['GET'])
    @staticmethod
    def get_books_by_name(request, str_variable):
        status_code, msg = book_controller.get_books_by_name_controller(request, str_variable)

        if status_code == 201: 
            return JsonResponse(msg, status=201, safe=False)
        else:
            return HttpResponse(f"Error: {msg}", status=status_code)
        
        
        


    #api/book_detail/{book_id}
    @api_view(['GET'])
    @staticmethod
    def get_book_by_id(request, book_id):
        status_code, msg = book_controller.get_book_by_id_controller(request, book_id)

        if status_code == 201: 
            return JsonResponse(msg, status=201, safe=False)
        else :
            return HttpResponse(f"Error: {msg}", status=status_code)
        


    #api/order/{json}
    @api_view(['PUT'])
    @staticmethod
    def place_order(request):
        status_code, msg = order_controller.place_order(request)

        if status_code == 200:
            return JsonResponse(msg, status=200)
        
        return HttpResponse(f'Error: {msg}', status=status_code)
       
       
