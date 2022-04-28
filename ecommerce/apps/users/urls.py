from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit/', views.edit_profile, name='edit'),
    path('address/create/', views.CreateAddressView.as_view(), name='create_address'),
    path('address/manage/', views.ManageAddressView.as_view(), name='manage_addresses'),
    path('address/delete/<int:pk>', views.DeleteAddressView.as_view(), name='delete_address'),
    path('address/update/<int:pk>', views.UpdateAddressView.as_view(), name='update_address'),
]
