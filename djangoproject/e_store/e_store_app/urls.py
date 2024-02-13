from django.urls import path
from .views import index, add_client, view_client, add_order, add_product, view_product, view_order, view_client_orders, view_client_products

urlpatterns = [
    path('', index, name='index'),
    path('add-client/', add_client, name='add_client'),
    path('view-client/', view_client, name='view_client'),
    path('add-order/', add_order, name='add_order'),
    path('view-order/<int:order_id>/', view_order, name='view_order'),
    path('add-product/', add_product, name='add_product'),
    path('view-product/', view_product, name='view_product'),
    path('view-client-orders/', view_client_orders, name='view_client_orders'),
    path('view-client-products/', view_client_products, name='view_client_products'),
]
