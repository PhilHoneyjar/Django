from django.core.management.base import BaseCommand
from djangoproject.e_store.e_store_app.models import Client


class Command(BaseCommand):
    help = 'Get all clients'

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        if clients:
            self.stdout.write("Clients:")
            for client in clients:
                self.stdout.write(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone Number: {client.phone_number}, Address: {client.address}")
        else:
            self.stdout.write("No clients found")
