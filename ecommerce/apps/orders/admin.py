from django.contrib import admin

from ecommerce.apps.orders.models import Order, OrderItem
from ecommerce.apps.payment.models import Payment


class ItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]
    extra = 0


class PaymentInline(admin.TabularInline):
    model = Payment
    can_delete = False
    readonly_fields = (
        "doc_number",
        "transaction_amount",
        "installments",
        "payment_method_id",
        "mercado_pago_id",
        "mercado_pago_status",
        "mercado_pago_status_detail",
    )
    ordering = ("id",)

    def has_add_permission(self, request, obj):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    inlines = [ItemInline, PaymentInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')
