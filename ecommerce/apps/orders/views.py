from django.db.models import Q
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from ecommerce.apps.cart.cart import Cart
from ecommerce.apps.orders.models import Order, OrderItem
from ecommerce.apps.users.models import Address
from ecommerce.apps.wish.models import Wish


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
            wish = Wish.objects.filter(Q(user=request.user) & Q(product=item['product'])).first()
            if wish:
                wish.delete()
        cart.clear()
        request.session['order_id'] = order.id
        return redirect('payment:process')
    return redirect('shop:home')
