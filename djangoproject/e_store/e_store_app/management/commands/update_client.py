from django.core.management.base import BaseCommand
from e_store_app.models import Client


class Command(BaseCommand):
    help = 'Updates an existing client'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('--name', type=str, help='New client name')
        parser.add_argument('--email', type=str, help='New client email')
        parser.add_argument('--phone_number', type=str, help='New client phone number')
        parser.add_argument('--address', type=str, help='New client address')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        updates = {k: v for k, v in kwargs.items() if v is not None and k != 'client_id'}

        if not updates:
            self.stderr.write('No updates provided')
            return

        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            self.stderr.write(f'Client with ID {client_id} does not exist')
            return

        for key, value in updates.items():
            setattr(client, key, value)

        client.save()
        self.stdout.write(self.style.SUCCESS(f'Client with ID {client_id} updated successfully'))
