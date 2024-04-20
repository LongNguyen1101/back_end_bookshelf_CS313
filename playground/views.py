from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from playground.controller.book_controller import book_controller
from playground.controller.order_controller import order_controller
from playground.controller.recommend_controller import recommend_controller


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
        
    # api/{category}
    @api_view(['GET'])
    @staticmethod
    def get_books_by_category(request, category):
        status_code, msg = book_controller.get_books_by_category_controller(request, category)

        if status_code == 201: 
            return JsonResponse(msg, status=201, safe=False)
        else:
            return HttpResponse(f"Error: {msg}", status=status_code)
        

    #api/book_detail/{book_id}
    @api_view(['GET'])
    @staticmethod
    def get_book_detail(request, book_id):
        status_code, msg = book_controller.get_book_detail_controller(request, book_id)

        if status_code == 201: 
            return JsonResponse(msg, status=201, safe=False)
        else :
            return HttpResponse(f"Error: {msg}", status=status_code)
        
    #api/category_list
    @api_view(['GET'])
    @staticmethod
    def get_category_list(request):
        status_code, msg = book_controller.get_category_list_controller(request)

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
       
    
    #api/book_recommend/{book_id}
    @api_view(['GET'])
    @staticmethod
    def get_book_recommend(request, book_id):
        status_code, msg = recommend_controller.get_book_recommend_controller(book_id)

        if status_code == 201:
            return JsonResponse(msg, status=status_code, safe=False)
        
        return HttpResponse(f'Error: {msg}', status=status_code)
    

    #api/book_recommend_cart/{book_id_list}
    @api_view(['GET'])
    @staticmethod
    def get_book_recommend_cart(request, book_id_list):
        status_code, msg = recommend_controller.get_book_recommend_cart_controller(book_id_list)

        if status_code == 201:
            return JsonResponse(msg, status=status_code, safe=False)
        
        return HttpResponse(f'Error: {msg}', status=status_code)
    

    #api/rules
    @api_view(['GET'])
    @staticmethod
    def get_rules(request):
        status_code, msg = recommend_controller.get_rules_controller()

        if status_code == 201:
            return JsonResponse(msg, status=status_code, safe=False)
        
        return HttpResponse(f'Error: {msg}', status=status_code)