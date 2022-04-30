from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'order',
        'transaction_amount',
        'mercado_pago_id',
        'mercado_pago_status',
        'mercado_pago_status_detail',
    ]
    list_filter = ['mercado_pago_status', ]
    search_fields = ['mercado_pago_id', ]
