from django.db import models

from ecommerce.apps.orders.models import Order
from ecommerce.apps.users.models import User


class Payment(models.Model):
    order = models.ForeignKey(Order, related_name='payments', on_delete=models.CASCADE)
    doc_number = models.CharField('CPF', max_length=15)
    email = models.EmailField('E-mail')
    transaction_amount = models.DecimalField(
        'Valor da Transação', max_digits=10, decimal_places=2
    )
    installments = models.IntegerField('Parcelas')
    payment_method_id = models.CharField('Método de Pagamento', max_length=250)
    mercado_pago_id = models.CharField(max_length=250, blank=True, db_index=True)
    mercado_pago_status = models.CharField(max_length=250, blank=True)
    mercado_pago_status_detail = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'Pagamento {self.id}'
