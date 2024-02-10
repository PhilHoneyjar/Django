from djangoproject.mysite.myapp.models import Product


def create_product(name, description, price, quantity):
    return Product.objects.create(name=name, description=description, price=price, quantity=quantity)


def get_all_products():
    return Product.objects.all()


def get_product_by_id(product_id):
    return Product.objects.get(id=product_id)


def update_product(product, **kwargs):
    for key, value in kwargs.items():
        setattr(product, key, value)
    product.save()
    return product


def delete_product(product):
    product.delete()
