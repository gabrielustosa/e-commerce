from django.views.generic import TemplateView

from ecommerce.apps.users.models import Address


class OrderCheckoutView(TemplateView):
    template_name = 'order/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.filter(user=self.request.user)
        return context


class OrderCheckoutDoneView(TemplateView):
    template_name = 'order/checkout_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = self.kwargs.get('order_id')
        return context
