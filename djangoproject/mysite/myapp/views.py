from django.shortcuts import render
from django.views import View
from .models import Client, Product, Order
from datetime import datetime, timedelta
import logging


class ClientOrdersView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'client_orders.html', {'clients': clients})


class ClientProductsView(View):
    def get(self, request):
        client = Client.objects.first()
        today = datetime.now()
        period = request.GET.get('period', '7')  # default period - week
        start_date = today - timedelta(days=int(period))
        orders = Order.objects.filter(client=client, order_date__gte=start_date, order_date__lte=today)
        products = Product.objects.filter(order__in=orders).distinct()
        return render(request, 'client_products.html', {'client': client, 'products': products})


logger = logging.getLogger(__name__)


def home(request):
    html_content = """
    <h1>Добро пожаловать на главную страницу!</h1>
    <p>Здесь вы найдете информацию о сайте, написанном с помощью Django.</p>
    <p>Описание о себе: <a href="/about">О себе</a></p>
    """

    # Логирование посещения
    logger.info("Пользователь посетил главную страницу")

    return render(request, 'myapp/home.html', {'html_content': html_content})


def about(request):
    html_content = """
    <h1>Обо мне</h1>
    <p>Сайт был создан с использованием Django.</p>
    <p>Надеюсь, верстка не уехала.</p>
    """

    # Логирование посещения
    logger.info("Пользователь посетил страницу 'О себе'")

    return render(request, 'myapp/about.html', {'html_content': html_content})
