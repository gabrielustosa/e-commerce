from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.views.decorators.http import require_POST

from ecommerce.apps.shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm
from ..wish.models import Wish


@require_POST
def cart_add(request, product_id):
    if request.user.is_anonymous:
        messages.error(request, 'Você precisa estar autênticado para comprar.')
        return redirect('shop:home')
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    else:
        cart.add(
            product=product,
            quantity=1,
        )
        Wish.objects.get(user=request.user, product=product).delete()
    return redirect('cart:detail')


@require_POST
def cart_remove(request, product_id):
    if request.user.is_anonymous:
        messages.error(request, 'Você precisa estar autênticado para comprar.')
        return redirect('shop:home')
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def cart_detail(request):
    if request.user.is_anonymous:
        messages.error(request, 'Você precisa estar autênticado para comprar.')
        return redirect('shop:home')
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})
