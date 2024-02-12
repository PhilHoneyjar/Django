from django.urls import path
from .views import index, create_client, view_client

urlpatterns = [
    path('', index, name='index'),
    path('create-client/', create_client, name='create_client'),
    path('view-client/<int:client_id>/', view_client, name='view_client'),
]
