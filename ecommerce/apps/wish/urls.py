from django.urls import path

from . import views

app_name = 'wish'

urlpatterns = [
    path('add/<int:product_id>/', views.wish_list_add, name='add'),
    path('remove/<int:wish_id>/', views.wish_list_delete, name='delete'),
]
