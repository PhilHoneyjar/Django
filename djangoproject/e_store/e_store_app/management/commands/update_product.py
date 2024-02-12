from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Product


class Command(BaseCommand):
    help = 'Updates an existing product'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='Product ID')
        parser.add_argument('--name', type=str, help='New product name')
        parser.add_argument('--description', type=str, help='New product description')
        parser.add_argument('--price', type=float, help='New product price')
        parser.add_argument('--quantity', type=int, help='New product quantity')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']
        updates = {k: v for k, v in kwargs.items() if v is not None and k != 'product_id'}

        if not updates:
            self.stderr.write('No updates provided')
            return

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            self.stderr.write(f'Product with ID {product_id} does not exist')
            return

        for key, value in updates.items():
            setattr(product, key, value)

        product.save()
        self.stdout.write(self.style.SUCCESS(f'Product with ID {product_id} updated successfully'))
