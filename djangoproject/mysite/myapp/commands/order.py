from djangoproject.mysite.myapp.models import Order


def create_order(client, products, total_amount):
    order = Order.objects.create(client=client, total_amount=total_amount)
    order.products.add(*products)
    order.calculate_total_amount()
    return order


def get_all_orders():
    return Order.objects.all()


def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)


def update_order(order, **kwargs):
    for key, value in kwargs.items():
        setattr(order, key, value)
    order.save()
    return order


def delete_order(order):
    order.delete()
