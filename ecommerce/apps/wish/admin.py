from django.contrib import admin

from ecommerce.apps.wish.models import Wish


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']
