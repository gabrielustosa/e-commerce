from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.AllProductsView.as_view(), name='home'),
    path('produto/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categoria/<slug:category_slug>/', views.ProductsCategoryView.as_view(), name='category_list'),
    path('buscar/', views.ProductSearchView.as_view(), name='search'),
    path('items/', views.OrderItemView.as_view(), name='items'),
]
