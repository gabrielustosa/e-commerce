from django.db import models

from ecommerce.apps.shop.models import Product
from ecommerce.apps.users.models import Address, User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Pedido {self.id}'

    def get_total_price(self):
        total_cost = sum(item.get_total_price() for item in self.items.all())
        return total_cost

    def get_description(self):
        return ', '.join(
            [f'{item.quantity}x {item.product.title}' for item in self.items.all()]
        )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        return self.price * self.quantity
