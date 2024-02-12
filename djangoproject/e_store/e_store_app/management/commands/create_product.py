from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Product


class Command(BaseCommand):
    help = 'Creates a new product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        description = kwargs['description']
        price = kwargs['price']
        quantity = kwargs['quantity']

        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" created successfully'))
