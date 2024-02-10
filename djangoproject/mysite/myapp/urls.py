from django.urls import path
from .views import home, about, ClientOrdersView, ClientProductsView

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('client_orders/', ClientOrdersView.as_view(), name='client_orders'),
    path('client_products/', ClientProductsView.as_view(), name='client_products')
]
