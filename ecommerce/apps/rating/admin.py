from django.contrib import admin

from ecommerce.apps.rating.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order', 'comment', 'rating')