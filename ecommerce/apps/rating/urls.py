from django.urls import path

from . import views

app_name = 'rating'

urlpatterns = [
    path('create/<int:item_order>/', views.CreateRatingView.as_view(), name='create')
]
