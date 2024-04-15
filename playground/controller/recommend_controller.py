from itertools import combinations
import json
from playground.controller.book_controller import book_controller

class recommend_controller:
    with open('playground/data/rules.json', "r") as f:
        data = json.load(f)

    def generate_combinations(book_id_list):
        numbers = book_id_list.split(', ')
        result = []

        for r in range(1, len(numbers) + 1):
            for comb in combinations(numbers, r):
                result.append(', '.join(comb))
        return result

    @classmethod
    def get_book_recommend_controller(cls, book_id):
        try:
            unique_book_ids = set()

            for item in cls.data:
                if item["base_items"] == book_id:
                    book_ids = item['add_items'].split(', ')
                    unique_book_ids.update(map(int, book_ids))

            books = []
            for book_id in unique_book_ids:
                status_code, msg = book_controller.get_books_by_id_controller(book_id)

                if status_code != 201:
                    return status_code, msg
                
                books.append(msg)

            return 201, books

        except Exception as e:
            return 500, e
        
    
    @classmethod
    def get_book_recommend_cart_controller(cls, book_id_list):
        try:
            book_id_list = cls.generate_combinations(book_id_list)
            unique_book_ids = set()

            for book_id in book_id_list:
                for item in cls.data:
                    if item["base_items"] == book_id:
                        book_ids = item['add_items'].split(', ')
                        unique_book_ids.update(map(int, book_ids))

            books = []
            for book_id in unique_book_ids:
                status_code, msg = book_controller.get_books_by_id_controller(book_id)

                if status_code != 201:
                    return status_code, msg
                
                books.append(msg)

            return 201, books

        except Exception as e:
            return 500, e
        

    @classmethod
    def get_rules_controller(cls):
        try:
            return 201, cls.data

        except Exception as e:
            return 500, e
    