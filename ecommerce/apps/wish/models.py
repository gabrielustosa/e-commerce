from django.db import models

from ecommerce.apps.shop.models import Product
from ecommerce.apps.users.models import User


class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
