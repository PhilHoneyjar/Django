from django.core.management.base import BaseCommand
from e_store_app.models import Order


class Command(BaseCommand):
    help = 'Get a specific order by ID'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']

        try:
            order = Order.objects.get(pk=order_id)
            self.stdout.write(
                f"ID: {order.id}, Client: {order.client}, Total Amount: {order.total_amount}, Order Date: {order.order_date}")
        except Order.DoesNotExist:
            self.stderr.write(f'Order with ID {order_id} does not exist')
