from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.OrderCheckoutView.as_view(), name='create'),
    path('checkout/<int:address_id>', views.order_process_view, name='checkout'),
    path('checkout_done/', views.OrderCheckoutDoneView.as_view(), name='checkout_done'),
]
