from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Order, Client, Product
from django.utils import timezone


class Command(BaseCommand):
    help = 'Creates a new order'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('product_ids', nargs='+', type=int, help='Product IDs')
        parser.add_argument('total_amount', type=float, help='Total amount')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        product_ids = kwargs['product_ids']
        total_amount = kwargs['total_amount']

        try:
            client = Client.objects.get(pk=client_id)
            products = Product.objects.filter(pk__in=product_ids)
            order = Order.objects.create(client=client, total_amount=total_amount, order_date=timezone.now())
            order.products.set(products)
            self.stdout.write(self.style.SUCCESS(f'Order #{order.id} created successfully'))
        except Client.DoesNotExist:
            self.stderr.write(f'Client with ID {client_id} does not exist')
        except Product.DoesNotExist:
            self.stderr.write('One or more products do not exist')
