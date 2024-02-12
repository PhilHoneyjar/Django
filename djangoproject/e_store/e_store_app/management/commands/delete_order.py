from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Order


class Command(BaseCommand):
    help = 'Deletes an existing order'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            self.stderr.write(f'Order with ID {order_id} does not exist')
            return

        order.delete()
        self.stdout.write(self.style.SUCCESS(f'Order with ID {order_id} deleted successfully'))
