from django.views.generic import ListView, TemplateView

from .models import Product
from ecommerce.apps.cart.forms import CartAddProductForm
from ..orders.models import OrderItem
from ..rating.models import Rating


class AllProductsView(ListView):
    template_name = 'shop/all_products.html'
    model = Product
    paginate_by = 6
    context_object_name = 'products'


class ProductsCategoryView(AllProductsView):
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        queryset = queryset.filter(category__slug=category_slug)
        return queryset


class ProductDetailView(TemplateView):
    template_name = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(pk=product_id)
        context['product'] = product
        context['ratings'] = Rating.objects.filter(order__product=product).select_related('user')
        context['form'] = CartAddProductForm()
        return context


class ProductSearchView(AllProductsView):
    def get_queryset(self, *args, **kwargs):
        term = self.request.GET.get('term') or self.request.session['term']
        queryset = super().get_queryset()

        if not term:
            return queryset

        self.request.session['term'] = term

        queryset = queryset.filter(title__icontains=term)

        self.request.session.save()
        return queryset


class OrderItemView(TemplateView):
    template_name = 'shop/order_item_view.html'

    def get_context_data(self, **kwargs):
        context = super(OrderItemView, self).get_context_data()
        context['items'] = OrderItem.objects.filter(order__user=self.request.user) \
            .prefetch_related('ratings') \
            .select_related('product')
        return context
