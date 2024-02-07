from django.shortcuts import render
import logging

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

