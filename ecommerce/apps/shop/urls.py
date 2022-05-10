from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.AllProductsView.as_view(), name='home'),
    path('product/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:category_slug>/', views.ProductsCategoryView.as_view(), name='category_list'),
    path('search/', views.ProductSearchView.as_view(), name='search'),
    path('items/', views.OrderItemView.as_view(), name='items'),
]
