from django.db import models

class Book(models.Model):
    ibsn13 = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    authors = models.CharField(max_length=100, blank=True, null=True)
    categories = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published_year = models.PositiveIntegerField(blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    num_pages = models.PositiveIntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.title
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        db_table = 'Order'

    def __str__(self):
        return f"Order {self.id} - Customer {self.customer.username}"

class OrderBook(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        db_table = 'OrderBook'

    def __str__(self):
        return f"Order Item {self.id} - Order {self.order.id} - Book {self.book.id}"
