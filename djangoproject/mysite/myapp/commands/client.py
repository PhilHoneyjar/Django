from djangoproject.mysite.myapp.models import Client


def create_client(name, email, phone_number, address):
    return Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)


def get_all_clients():
    return Client.objects.all()


def get_client_by_id(client_id):
    return Client.objects.get(id=client_id)


def update_client(client, **kwargs):
    for key, value in kwargs.items():
        setattr(client, key, value)
    client.save()
    return client


def delete_client(client):
    client.delete()
