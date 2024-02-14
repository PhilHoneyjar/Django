<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Product, Order
from django.http import HttpResponse
from .forms import ClientForm, ProductForm
from datetime import datetime, timedelta
=======
from django.shortcuts import render, redirect
from .models import Client
from django.http import HttpResponse
from .forms import ClientForm
>>>>>>> main


def index(request):
    return render(request, 'index.html')


<<<<<<< HEAD
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})


def view_client(request):
    client_id = request.GET.get('client_id')
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'view_client.html', {'client': client})


def add_order(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        products_ids = request.POST.getlist('products')
        total_amount = request.POST.get('total_amount')

        client = Client.objects.get(id=client_id)
        products = Product.objects.filter(id__in=products_ids)

        order = Order.objects.create(client=client, total_amount=total_amount)
        order.products.set(products)
        return redirect('index')
    else:
        clients = Client.objects.all()
        products = Product.objects.all()
        return render(request, 'add_order.html', {'clients': clients, 'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def view_product(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'view_product.html', {'product': product})


def view_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'view_order.html', {'order': order})


def view_client_orders(request):
    client_id = request.GET.get('client_id')
    client = get_object_or_404(Client, id=client_id)
    orders = client.orders.all()
    return render(request, 'view_client_orders.html', {'client': client, 'orders': orders})


def view_client_products(request):
    client_id = request.GET.get('client_id')
    filter_days = int(request.GET.get('filter', 7))

    client = get_object_or_404(Client, id=client_id)

    # Определяем дату начала периода в зависимости от выбранного фильтра
    start_date = datetime.now() - timedelta(days=filter_days)

    # Получаем все заказы клиента за указанный период
    orders = Order.objects.filter(client=client, order_date__gte=start_date)

    # Получаем все товары из заказов
    products = []
    for order in orders:
        products.extend(order.products.all())

    return render(request, 'view_client_products.html', {'client': client, 'products': products})
=======
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


>>>>>>> main
