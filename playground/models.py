from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    published_year = models.PositiveIntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    cover = models.ImageField(upload_to='data/images/books/', blank=True, null=True)
    unit_price = models.PositiveIntegerField(blank=True, default=0)
    stock = models.PositiveIntegerField(blank=True, default=0)
    
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

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(blank=True, default=0)

    class Meta:
        db_table = 'OrderItem'

    def __str__(self):
        return f"Order Item {self.id} - Order {self.order.id} - Book {self.book.id}"
