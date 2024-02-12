from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Order, Client, Product
from django.utils import timezone


class Command(BaseCommand):
    help = 'Updates an existing order'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')
        parser.add_argument('--client_id', type=int, help='New client ID')
        parser.add_argument('--product_ids', nargs='+', type=int, help='New product IDs')
        parser.add_argument('--total_amount', type=float, help='New total amount')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        updates = {k: v for k, v in kwargs.items() if v is not None and k != 'order_id'}

        if not updates:
            self.stderr.write('No updates provided')
            return

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            self.stderr.write(f'Order with ID {order_id} does not exist')
            return

        if 'client_id' in updates:
            try:
                client = Client.objects.get(pk=updates['client_id'])
                order.client = client
            except Client.DoesNotExist:
                self.stderr.write(f'Client with ID {updates["client_id"]} does not exist')

        if 'product_ids' in updates:
            try:
                products = Product.objects.filter(pk__in=updates['product_ids'])
                order.products.set(products)
            except Product.DoesNotExist:
                self.stderr.write('One or more products do not exist')

        for key, value in updates.items():
            if key != 'client_id' and key != 'product_ids':
                setattr(order, key, value)

        order.save()
        self.stdout.write(self.style.SUCCESS(f'Order with ID {order_id} updated successfully'))
