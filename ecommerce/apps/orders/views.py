from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from ecommerce.apps.cart.cart import Cart
from ecommerce.apps.orders.models import Order, OrderItem
from ecommerce.apps.users.models import Address


class OrderCheckoutView(TemplateView):
    template_name = 'order/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.filter(user=self.request.user)
        return context


@require_POST
def order_process_view(request, address_id):
    address = Address.objects.all().get(pk=address_id)
    order = Order.objects.create(address=address, user=request.user)
    cart = Cart(request)
    if cart:
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'],
            )
        cart.clear()
        request.session['order_id'] = order.id
    return redirect('order:checkout_done')


class OrderCheckoutDoneView(TemplateView):
    template_name = 'order/checkout_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.kwargs.get('order_id')
        return context
