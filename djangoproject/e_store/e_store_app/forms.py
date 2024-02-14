from django import forms
<<<<<<< HEAD
from .models import Client, Product
=======
from .models import Client
>>>>>>> main


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone_number', 'address']
<<<<<<< HEAD


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'date_added']
=======
>>>>>>> main
