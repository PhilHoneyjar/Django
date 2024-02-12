from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Client


class Command(BaseCommand):
    help = 'Get a specific client by ID'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']

        try:
            client = Client.objects.get(pk=client_id)
            self.stdout.write(
                f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone Number: {client.phone_number}, Address: {client.address}")
        except Client.DoesNotExist:
            self.stderr.write(f'Client with ID {client_id} does not exist')
