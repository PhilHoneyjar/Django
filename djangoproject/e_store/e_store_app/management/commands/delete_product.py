from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Product


class Command(BaseCommand):
    help = 'Deletes an existing product'

    def add_arguments(self, parser):
        parser.add_argument('product_id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        product_id = kwargs['product_id']

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            self.stderr.write(f'Product with ID {product_id} does not exist')
            return

        product.delete()
        self.stdout.write(self.style.SUCCESS(f'Product with ID {product_id} deleted successfully'))
