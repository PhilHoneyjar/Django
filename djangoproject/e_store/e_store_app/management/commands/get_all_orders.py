from django.core.management.base import BaseCommand
from e_store_app.models import Order


class Command(BaseCommand):
    help = 'Get all orders'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        if orders:
            self.stdout.write("Orders:")
            for order in orders:
                self.stdout.write(f"ID: {order.id}, Client: {order.client}, Total Amount: {order.total_amount}, Order Date: {order.order_date}")
        else:
            self.stdout.write("No orders found")
