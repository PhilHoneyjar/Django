from django.shortcuts import render, redirect
from .models import Client
from django.http import HttpResponse
from .forms import ClientForm


def index(request):
    return render(request, 'index.html')


def create_client(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        client = Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return redirect('view_client', client_id=client.id)
    else:
        return render(request, 'create_client.html')


def view_client(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'view_client.html', {'client': client})


