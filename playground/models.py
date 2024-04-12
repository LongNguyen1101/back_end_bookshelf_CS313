from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100, blank=True, null=True)
    categories = models.CharField(max_length=100, blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    published_year = models.CharField(max_length=50, blank=True, null=True)
    average_rating = models.FloatField(blank=True, null=True)
    num_pages = models.PositiveIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    
    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.title
    
class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'PurchaseOrder'

    def __str__(self):
        return f"Order {self.id} - Customer {self.customer.username}"

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        db_table = 'OrderDetail'

    def __str__(self):
        return f"Order Item {self.id} - Order {self.order.id} - Book {self.book.id}"
