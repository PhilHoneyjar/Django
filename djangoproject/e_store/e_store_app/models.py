from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Client:{self.name}, email :{self.email}, phone:{self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)

    def __str__(self):
        return f'Product {self.name}, price: {self.price}, quantity: {self.quantity}'

    @property
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all())


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def calculate_total_amount(self):
        total = sum(product.price for product in self.products.all())
        self.total_amount = total
        self.save()
