from random import uniform, randint

from django.core.management.base import BaseCommand
from e_store_app.models import Product


class Command(BaseCommand):
    help = "Generate random products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of random products')

    def handle(self, *args, **kwargs):
        products = []
        count = kwargs.get('count')
        for i in range(1, count + 1):
            products.append(Product(
                name=f'Product # {i}',
                description='Some product properties',
                price=uniform(0.01, 999999.99),
                quantity=randint(1, 10000)
            ))
        Product.objects.bulk_create(products)
