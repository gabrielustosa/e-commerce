from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('process/', views.PaymentCreateView.as_view(), name='process'),
    path('failure/', views.PaymentFailureView.as_view(), name='failure'),
    path('pending/', views.PaymentPendingView.as_view(), name='pending'),
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('webhook/', views.payment_webhook, name='webhook'),
]
