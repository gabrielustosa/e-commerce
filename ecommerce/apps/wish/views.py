from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import resolve
from django.views.decorators.http import require_POST

from ecommerce.apps.shop.models import Product
from ecommerce.apps.wish.models import Wish


@require_POST
def wish_list_add(request, product_id):
    if request.user.is_anonymous:
        messages.error(request, 'Você precisa estar logado para adicionar produtos na sua lista de desejos.')
        return redirect('shop:home')
    product = Product.objects.get(id=product_id)
    if not product:
        return redirect('shop:home')
    wish = Wish.objects.filter(Q(user=request.user) & Q(product__id=product_id))
    if wish:
        messages.error(request, 'Você já tem esse produto na sua lista desejos.')
        return redirect('shop:home')
    Wish.objects.create(user=request.user, product=product)
    messages.success(request, 'Produto adicionando a sua lista de desejos.')
    return redirect('shop:home')


@require_POST
def wish_list_delete(request, wish_id):
    if request.user.is_anonymous:
        messages.error(request, 'Você precisa estar logado para deletar produtos na sua lista de desejos.')
        return redirect('shop:home')
    wish = Wish.objects.get(id=wish_id)
    if wish.user != request.user:
        return redirect('shop:home')
    wish.delete()
    messages.success(request, f'Produto removido da sua lista de desejos.')
    return redirect('shop:home')
