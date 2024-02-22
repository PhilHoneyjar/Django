from django.contrib import admin
from .models import Client, Order, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'registration_date')
    search_fields = ('name', 'email', 'phone')


admin.site.register(Client, ClientAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('client__name', 'products__name')


admin.site.register(Order, OrderAdmin)
