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

            # # Create or retrieve user's order
            order, _ = models.Order.objects.get_or_create()

            # # Iterate through each item in the list and create or update order items
            for item in items:
                product_type = item.get('product_type')
                quantity = item.get('quantity')
                product_id = item.get('product_id')

            #     # Check the product type and retrieve the product from the database
                if product_type == 'book':
                    product = get_object_or_404(models.Book, id=product_id)
            #     # elif product_type == 'office_supplies':
            #     #     product = get_object_or_404(models.OfficeSupply, id=product_id)
                else:
                    return 400, f'Invalid product type: {product_type}'
                
            #     product.stock -= quantity

            #     # Create or update order item
                order_item, _ = models.OrderBook.objects.get_or_create(order=order, book=product)
                order_item.quantity = quantity
                price += product.unit_price * quantity
                order_item.save()
                product.save()

            order.total = price
            order.save()

            return 200, 'success'
    
        except json.JSONDecodeError:
            return 400, 'Invalid JSON format'
