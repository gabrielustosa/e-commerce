from django.contrib import admin

from ecommerce.apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('id', 'order')
