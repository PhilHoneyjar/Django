from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Product


class Command(BaseCommand):
    help = 'Get all products'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        if products:
            self.stdout.write("Products:")
            for product in products:
                self.stdout.write(f"ID: {product.id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}")
        else:
            self.stdout.write("No products found")
