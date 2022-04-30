from django.db import models
from django.db.models import Avg

from ecommerce.apps.users.models import User


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ('created',)

    def in_stock(self):
        return self.stock != 0

    def get_rating_avg(self):
        from ecommerce.apps.rating.models import Rating
        result = Rating.objects.filter(order__product=self).aggregate(Avg('rating'))
        result = result['rating__avg']
        if result:
            return round(result)
        return 0

    def __str__(self):
        return self.title
