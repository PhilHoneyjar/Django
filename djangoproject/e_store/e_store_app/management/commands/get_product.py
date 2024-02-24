from django.core.management.base import BaseCommand
from e_store_app.models import Product


class Command(BaseCommand):
    help = 'Get a specific product by ID'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']

        try:
            product = Product.objects.get(pk=product_id)
            self.stdout.write(
                f"ID: {product.id}, Name: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}")
        except Product.DoesNotExist:
            self.stderr.write(f'Product with ID {product_id} does not exist')
