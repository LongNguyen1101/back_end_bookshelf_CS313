from playground import models
from django.shortcuts import get_object_or_404
import json

class order_controller:
    def place_order(request):
        price = 0

        try:
            # Get JSON from request
            data = json.loads(request.body)

            # Get list of items from JSON
            items = data.get('items', [])

            if items is None: return 400, 'Invalid JSON format'

            # # Create or retrieve user's order
            order, _ = models.PurchaseOrder.objects.get_or_create()

            # # Iterate through each item in the list and create or update order items
            for item in items:
                product_id = item.get('book_id')
                quantity = item.get('quantity')

                book = get_object_or_404(models.Book, book_id=product_id)

                # Create or update order item
                order_item, _ = models.OrderDetail.objects.get_or_create(order=order, book=book)
                order_item.quantity = quantity
                price += book.price * quantity
                order_item.save()

            order.total = round(price, 2)
            order.save()

            response = {
                'id': order.id,
                'total': order.total
            }

            return 200, response
    
        except Exception as e:
            return 500, e