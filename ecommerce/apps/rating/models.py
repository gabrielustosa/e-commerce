from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from ecommerce.apps.orders.models import OrderItem
from ecommerce.apps.users.models import User


class Rating(models.Model):
    order = models.ForeignKey(OrderItem, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    comment = models.TextField()
