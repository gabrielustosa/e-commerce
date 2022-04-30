from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ecommerce.apps.orders.models import OrderItem
from ecommerce.apps.rating.models import Rating


class CreateRatingView(CreateView):
    template_name = 'rating/create.html'
    model = Rating
    fields = ('rating', 'comment')
    success_url = reverse_lazy('shop:items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.order = OrderItem.objects.get(pk=self.kwargs.get('item_order'))
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        item = OrderItem.objects.get(pk=self.kwargs.get('item_order'))
        if item.ratings.exists():
            raise Http404()
        if item.order.user != request.user:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
